import pandas as pd
import soccerdata as sd

from pydantic import ValidationError
from supabase import create_client

from src.pydantic_models import *
from src.common.constants import *
from src.common.config import SUPABASE_PROJECT_URL, SUPABASE_API_KEY

def scrape_fbref_data():     
    # Get minimum shared start and end year for all leagues available in fbref
    fbref = sd.FBref(leagues=BIG_5_EUROPEAN_LEAGUES_COMBINED, proxy="tor")
    df = fbref.read_leagues()
    start_season = "9900"
    end_season = "2324"
    
    # Generate list of seasons from start to end season
    seasons = generate_season_list(start_season, end_season)
    
    scrape_team_season_stats(seasons)

def scrape_team_season_stats(seasons):
    for season in seasons:
        fbref = sd.FBref(leagues=SOCCERDATA_LEAGUES, seasons=season, proxy="tor", no_cache=True)
        for stat_type in FBREF_STAT_CATEGORIES:  
            df = fbref.read_team_season_stats(stat_type=stat_type, opponent_stats=False)
            df = df.reset_index()
            df = df.drop_duplicates()
            
            model = STAT_CATEGORY_TEAM_MODELS.get(stat_type)
            table_name = STAT_CATEGORY_TEAM_TABLE_NAMES.get(stat_type)
            
            if model and table_name:
                # Map DataFrame to Pydantic model and validate
                instances = []
                for _, row in df.iterrows():
                    try:
                        instance = model.from_df(row)
                        instances.append(instance)
                    except ValidationError as e:
                        print(f"Validation error for {stat_type}:", e)
                
                # Upload validated instances to Supabase table
                upload_to_supabase_table(table_name, instances)

def upload_to_supabase_table(table_name, instances):
    supabase = create_client(SUPABASE_PROJECT_URL, SUPABASE_API_KEY)
    
    # Upload instances to Supabase table
    for instance in instances:
        supabase.table(table_name).insert(instance.dict()).execute()
    
def generate_season_list(start_season, end_season):
    # Convert integers to strings
    start_season_str = str(start_season)
    end_season_str = str(end_season)

    # Extract the centuries and years, assuming the format is YYXX where XX is YY+1
    start_century = int(start_season_str[:2])  # Get the century part (first two digits)
    end_century = int(end_season_str[:2])  # Get the century part (first two digits)

    # Construct the full years from the century part
    start_year = 1900 + start_century
    end_year = 2000 + end_century + 1  # +1 because we include the next season's start year

    # Generate the seasons list
    seasons = []
    for year in range(start_year, end_year + 1):
        next_year = year + 1
        # Format each year pair as 'YYYY-YYYY' to ensure consistency
        season = f'{year % 100:02d}{next_year % 100:02d}'
        seasons.append(season)

    return seasons