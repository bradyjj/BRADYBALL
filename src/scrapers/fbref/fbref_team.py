import pandas as pd
import soccerdata as sd
import logging
import csv
import re

from tqdm import tqdm
from pydantic import ValidationError
from .fbref_util import *

from src.common import *

def scrape_fbref_team_data():
    # Get minimum shared start and end year for all leagues available in fbref
    fbref = sd.FBref(leagues=BIG_5_EUROPEAN_LEAGUES_COMBINED, proxy=None)
    df = fbref.read_leagues()
    start_season = "2223"
    end_season = "2324"

    # Generate list of seasons from start to end season
    seasons = generate_season_list(start_season, end_season)

    scrape_team_season_stats(seasons)


def scrape_team_season_stats(seasons):
    for season in tqdm(seasons, desc="Scraping seasons"):
        logging.info(f"Processing season: {season}")
        fbref = sd.FBref(leagues=SOCCERDATA_LEAGUES,
                         seasons=season, no_cache=False)

        for stat_type in FBREF_STAT_CATEGORIES:
            logging.info(f"Reading data for stat type: {stat_type}")
            failed_rows = []
            try:
                df = fbref.read_team_season_stats(
                    stat_type=stat_type, opponent_stats=False)
                df = df.reset_index()
                df = df.drop_duplicates()

                model = FBREF_STAT_CATEGORY_TEAM_MODELS.get(stat_type)
                table_name = STAT_CATEGORY_TEAM_TABLE_NAMES.get(stat_type)
                mapping = FBREF_TEAM_MODELS_MAPPINGS.get(model)

                df.columns = [mapping.get((col,) if isinstance(
                    col, str) else col, col) for col in df.columns]

                logging.info(f"Columns after mapping: {df.columns.tolist()}")

                if model and table_name:
                    instances = []
                    for _, row in df.iterrows():
                        try:
                            logging.info(f"Processing row for {
                                         stat_type}: {row.to_dict()}")
                            instance = from_df_to_model(
                                row, model, season, mapping)
                            if instance is not None:
                                instances.append(instance)
                            else:
                                logging.error(f"Failed to create model instance from row: {
                                              row.to_dict()}")
                                failed_rows.append(row.to_dict())
                        except ValidationError as e:
                            logging.error(f"Validation error for {
                                          stat_type}: {e}")
                            failed_rows.append(row.to_dict())
                            continue
                        except Exception as e:
                            logging.error(f"Unexpected error during model instantiation for {
                                          stat_type}: {e}")
                            failed_rows.append(row.to_dict())
                            continue

                    upload_to_supabase_table(table_name, instances)
                    logging.info(f"Uploaded data for {stat_type} to {
                                 table_name} successfully.")
            except Exception as e:
                logging.error(f"Error processing {
                              stat_type} for season {season}: {e}")
                continue

            if failed_rows:
                write_failed_rows_to_csv(failed_rows, stat_type)


def from_df_to_model(row, model, season, mapping):
    # Convert the row to a dictionary using the column mapping
    data = {str(mapping.get((key,) if isinstance(key, str) else key, key)): (None if pd.isna(value) else value)
            for key, value in row.items()}

    if 'age' in data and isinstance(data['age'], str):
        age_str = data['age']
        # Extract and convert the age part
        age_int = int(age_str.split('-')[0])
        data['age'] = age_int

    if 'url' in data:
        team_id = extract_team_id(data['url'])
        if team_id:
            data['team_id'] = team_id

    try:
        return model(**data)
    except (ValueError, IndexError, TypeError) as e:
        logging.error(f"{str(e)}")
        return None


def extract_team_id(url):
    match = re.search(r'/squads/([^/]+)/', url)
    return match.group(1) if match else None


def write_failed_rows_to_csv(failed_rows, stat_type):
    keys = failed_rows[0].keys()
    filename = f'teams-{stat_type}-failed.csv'
    with open(filename, 'w', newline='') as output_file:
        dict_writer = csv.DictWriter(output_file, fieldnames=keys)
        dict_writer.writeheader()
        dict_writer.writerows(failed_rows)
