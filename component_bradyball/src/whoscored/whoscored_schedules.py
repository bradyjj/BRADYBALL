import os
import re
import pandas as pd

from typing import List
from datetime import datetime
from supabase import create_client, Client
from pydantic import ValidationError
from src.pydantic_models.match import Match
from src.common.constants import WHOSCORED_MATCH_URL_TEMPLATE, WHOSCORED_URL_TO_CONST
from src.common.config import SUPABASE_PROJECT_URL, SUPABASE_API_KEY

def extract_season_and_league(url):
    pattern = WHOSCORED_MATCH_URL_TEMPLATE.replace('{match_id}', r'\d+')
    pattern = pattern.replace('{league}', r'(?P<league>[^-]+(?:-[^-]+)*)')
    pattern = pattern.replace('{season}', r'(?P<season>\d{4}-\d{4})')
    pattern = pattern.replace('{teams}', r'.+')

    # Use the regex to search the URL
    match = re.search(pattern, url)
    if match:
        league_key = match.group('league')
        # Replace hyphens with spaces and match against the constants map
        league = WHOSCORED_URL_TO_CONST.get(league_key.replace('-', ' '), league_key.replace('-', ' '))
        return match.group('season'), league
    else:
        return None, None
    
def process_schedule(df, rejected_df):
    for index, row in df.iterrows():
        if pd.notna(row['url']):
            season, league = extract_season_and_league(row['url'])
            if season and league:
                start_date, start_time = split_date_time(row['date'])
                df.at[index, 'start_date'] = start_date
                df.at[index, 'start_time'] = start_time
                df.at[index, 'season'] = season
                df.at[index, 'league'] = league
                df.at[index, 'whoscored_url'] = row['url']
            else:
                rejected_df = rejected_df.append(row)
        else:
            rejected_df = rejected_df.append(row)
    return df, rejected_df

def upload_schedule_to_db(df: pd.DataFrame):
    supabase: Client = create_client(SUPABASE_PROJECT_URL, SUPABASE_API_KEY)
    validated_data = []

    for _, row in df.iterrows():
        try:
            match = Match(**row)
            validated_data.append(match.dict(exclude_unset=True))
        except ValidationError as e:
            print(f"Error validating data: {e}")

    if validated_data:
        response = supabase.table('matches').insert(validated_data).execute()
        print("Data uploaded successfully!" if response.status_code == 201 else "Failed to upload data")
    else:
        print("No valid data to upload.")

def split_date_time(date_str):
    dt = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
    return dt.strftime("%Y-%m-%d"), dt.strftime("%H:%M:%S")

def load_schedules():
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
            processed_df, rejected_df = process_schedule(df, rejected_df)
            all_dfs.append(processed_df)

    # Combine all dfs and upload to df
    combined_df = pd.concat(all_dfs, ignore_index=True)
    upload_schedule_to_db(combined_df)

    # Save csv for failed matches to be added
    if not rejected_df.empty:
        rejected_csv_path = os.path.join(directory_path, 'rejected-schedules.csv')
        rejected_df.to_csv(rejected_csv_path, index=False)
        print(f"Rejected schedules saved to {rejected_csv_path}")