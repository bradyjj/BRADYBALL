import os
import re
import pandas as pd

from typing import List
from datetime import datetime
from supabase import create_client, Client
from pydantic import ValidationError
from tqdm import tqdm
from src.pydantic_models.match import Match
from src.common.constants import WHOSCORED_MATCH_URL_TEMPLATE, WHOSCORED_URL_TO_CONST
from src.common.config import SUPABASE_PROJECT_URL, SUPABASE_API_KEY

def extract_season_and_league(url):
    # Using non-greedy quantifiers to ensure it stops at the first occurrence of a year pattern
    pattern = re.escape(WHOSCORED_MATCH_URL_TEMPLATE).replace(r'\{match_id\}', r'\d+')
    pattern = pattern.replace(r'\{page\}', r'(?P<page>live)')
    pattern = pattern.replace(r'\{league\}', r'(?P<league>[\w\s-]+?)')  # Non-greedy to stop before the year
    pattern = pattern.replace(r'\{season\}', r'(?P<season>\d{4}-\d{4})')
    pattern = pattern.replace(r'\{teams\}', r'(?P<teams>.+)')

    # Use the regex to search the URL
    match = re.search(pattern, url)
    if match:
        league_key = match.group('league')
        season = match.group('season')
        teams = match.group('teams')

        # Handling potential edge cases in league names like "Germany Bundesliga 2003" mistakenly captured
        # Using a second regex to ensure we stop at a number sequence indicating a season year
        league_match = re.search(r'^(.*?)(?=\s\d{4}-\d{4})', league_key)
        if league_match:
            league_key = league_match.group(0)

        # Replace hyphens with spaces and match against the constants map
        league = WHOSCORED_URL_TO_CONST.get(league_key.strip().replace('-', ' '), league_key.strip().replace('-', ' '))

        return season, league
    else:
        return None, None
    
def preprocess_url(url):
    expected_url = WHOSCORED_MATCH_URL_TEMPLATE.replace('{page}', 'live')

    if expected_url in url:
        return url

    # Replace anything other than '/live' with '/live' in the page spot
    return re.sub(r'/(?!(?:.*/)?live(?:/.*)?$)[^/]+(?=/[^/]*$)', '/live', url)

def process_schedule(df, rejected_df):
    for index, row in df.iterrows():
        url = preprocess_url(row['url']) if pd.notna(row['url']) else None
        if url:
            season, league = extract_season_and_league(url)
            if season and league:
                start_date, start_time = split_date_time(row['date'])
                df.at[index, 'start_date'] = start_date
                df.at[index, 'start_time'] = start_time
                df.at[index, 'season'] = season
                df.at[index, 'league'] = league
                df.at[index, 'whoscored_url'] = url
            else:
                rejected_df = rejected_df.append(row, ignore_index=True)
        else:
            rejected_df = rejected_df.append(row, ignore_index=True)
    return df, rejected_df

def print_progress(iteration, total, prefix='', suffix='', decimals=1, length=50, fill='█'):
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    bar = fill * filled_length + '-' * (length - filled_length)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end="\r")
    # Print New Line on Complete
    if iteration == total: 
        print()

def upload_schedule_to_db(df: pd.DataFrame):
    supabase: Client = create_client(SUPABASE_PROJECT_URL, SUPABASE_API_KEY)
    batch_size = 50  # Define the batch size
    num_batches = (len(df) + batch_size - 1) // batch_size

    print("Uploading data in batches...")
    for i in tqdm(range(num_batches), desc="Uploading batches"):
        batch_df = df[i * batch_size:(i + 1) * batch_size]
        validated_data = []

        for _, row in batch_df.iterrows():
            try:
                match = Match(**row)
                validated_data.append(match.dict(exclude_unset=True))
                # Print each row before uploading
                print(f"Uploading row: {match.dict(exclude_unset=True)}")
            except ValidationError as e:
                print(f"\nError validating data in batch {i+1}: {e}")
                continue

        if validated_data:
            try:
                response = supabase.table('match').insert(validated_data).execute()
                if response.error:
                    print(f"\nFailed to upload batch {i+1}: {response.error.message}")
            except Exception as e:
                print(f"\nException during upload of batch {i+1}: {e}")
        else:
            print(f"\nNo valid data to upload in batch {i+1}.")

    print("Upload complete.")

def split_date_time(date_str):
    dt = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
    return dt.strftime("%Y-%m-%d"), dt.strftime("%H:%M:%S")

def load_whoscored_schedules():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    directory_path = os.path.join(current_dir, 'schedules')
    if not os.path.exists(directory_path):
        print("Directory not found:", directory_path)
        return

    # List of df to upload to db
    all_dfs = []

    # Stores all rows that fail to be uploaded
    rejected_df = pd.DataFrame()

    # For each schedule process csv and save in df
    for filename in os.listdir(directory_path):
        if filename.endswith('.csv'):
            file_path = os.path.join(directory_path, filename)
            df = pd.read_csv(file_path)

            # Rename 'game_id' column to 'match_id' to fit db model
            df.rename(columns={'game_id': 'match_id'}, inplace=True)
            row_count = df.shape[0]
            print("Number of rows:", row_count)
            
            # Replace null values in 'stage' column with "None"
            df['stage'] = df['stage'].astype(str).fillna('None')

            processed_df, rejected_df = process_schedule(df, rejected_df)
            all_dfs.append(processed_df)

    # Combine all dfs and upload to df
    combined_df = pd.concat(all_dfs, ignore_index=True)
    #upload_schedule_to_db(combined_df)

    # Save csv for failed matches to be added
    if not rejected_df.empty:
        rejected_csv_path = os.path.join(directory_path, 'rejected-schedules.csv')
        rejected_df.to_csv(rejected_csv_path, index=False)
        print(f"Rejected schedules saved to {rejected_csv_path}")