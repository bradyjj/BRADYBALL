import logging
from src.common.config import SUPABASE_URL, SUPABASE_KEY
from supabase import create_client


def generate_season_list(start_season, end_season):
    def convert_to_full_year(yy):
        year = int(yy)
        if year < 90:
            return 2000 + year
        else:
            return 1900 + year

    start_year = convert_to_full_year(start_season[:2])
    end_year = convert_to_full_year(end_season[:2])

    seasons = []
    year = start_year
    while year <= end_year:
        next_year = year + 1
        season = f'{year % 100:02d}{next_year % 100:02d}'
        seasons.append(season)
        year += 1

    return seasons


def upload_to_supabase_table(table_name, instances):
    supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

    # Upload instances to Supabase table
    for instance in instances:
        try:
            supabase.table(table_name).insert(instance.dict()).execute()
        except Exception as e:
            logging.error(f"Failed to upload instance to {table_name}: {e}")
