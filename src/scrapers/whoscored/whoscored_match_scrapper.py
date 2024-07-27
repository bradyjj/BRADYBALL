import json
import numpy as np
import pandas as pd

from bs4 import BeautifulSoup
from selenium import webdriver
from supabase import create_client

from common.pydantic_models.match_event import MatchEvent
from src.common.config import SUPABASE_URL, SUPABASE_KEY

def main():
    whoscored_urls = get_whoscored_urls()
    scrape_urls(whoscored_urls)

def get_whoscored_urls():
    urls = []
    return urls

def scrape_urls(urls):
    driver = webdriver.Chrome()

    for url in urls:
        soup = scrape_website(driver, url)
        match_data = get_match_data(soup)
    
        upload_to_supabase(match_data)

def is_match_events_valid(match_events):
    for x in match_events.to_dict(orient="records"):
        try:
            MatchEvent(**x).dict()
        except Exception as e:
            return False
    return True

def scrape_website(driver, url):
    driver.get(url)
    return BeautifulSoup(driver.page_source, 'html.parser')

def get_match_data(soup): 
    element = soup.select_one('script:-soup-contains("matchCentreData")')
    return json.loads(element.text.split("matchCentreData: ")[1].split(',\n')[0])

def rename_cols(df):
    # Rename df columns
    return df.rename(
        {
            'eventId': 'event_id',
            'expandedMinute': 'expanded_minute',
            'outcomeType': 'outcome_type',
            'isTouch': 'is_touch',
            'playerId': 'player_id',
            'teamId': 'team_id',
            'endX': 'end_x',
            'endY': 'end_y',
            'blockedX': 'blocked_x',
            'blockedY': 'blocked_y',
            'goalMouthZ': 'goal_mouth_z',
            'goalMouthY': 'goal_mouth_y',
            'isShot': 'is_shot',
            'cardType': 'card_type',
            'isGoal': 'is_goal'
        },
        axis=1
    )

def convert_data_types(df):
    df[['id', 'event_id', 'minute', 'team_id', 'player_id']] = df[['id', 'event_id', 'minute', 'team_id', 'player_id']].astype(int)
    df[['second', 'x', 'y', 'end_x', 'end_y']] = df[['second', 'x', 'y', 'end_x', 'end_y']].astype(float)
    df[['is_shot', 'is_goal', 'card_type']] = df[['is_shot', 'is_goal', 'card_type']].astype(bool)
    return df

def clean_df(df):
    # Drop rows without a playerId assigned
    df.dropna(subset='playerId', inplace=True)

    # Replace all NaN values with None values
    df = df.where(pd.notnull(df), None)

    # Reanme cols to fit python naming convention
    df = rename_cols(df)

    # Drop columns we do not need
    df.drop(columns=["period", "type", "outcome_type"], inplace=True)

    # Convert data types
    df = convert_data_types(df)

    # Replace NaN boolean values with False
    df['is_goal'] = df['is_goal'].fillna(False)
    df['is_shot'] = df['is_shot'].fillna(False)

    # Replace all NaN values in floats with None
    for column in df.columns:
        if df[column].dtype == np.float64 or df[column].dtype == np.float32:
            df[column] = np.where(
                np.isnan(df[column]),
                None,
                df[column]
            )
    
    return df

def upload_to_supabase(match_data):
    supabase = create_client(SUPABASE_PROJECT_URL, SUPABASE_API_KEY)

    # Get match event data
    match_events = match_data['events']

    # Clean match_event
    match_event_df = pd.DataFrame(match_events)
    match_event_df = clean_df(match_event_df)

    # Insert match data
    generated_match_id = insert_match(match_events, supabase)

    # Insert match events
    if generated_match_id is not None:
        insert_match_events(match_event_df, generated_match_id, supabase)

    # Get team info
    team_info = get_team_info(match_data)

    # Insert players
    insert_players(team_info, supabase)

def get_team_info(match_data):
    team_info = []

    # Home team info
    team_info.append({
        'team_id': match_data['home']['teamId'],
        'name': match_data['home']['name'],
        'country_name': match_data['home']['countryName'],
        'manager_name': match_data['home']['managerName'],
        'players': match_data['home']['players'],
    })

    # Away team info
    team_info.append({
        'team_id': match_data['away']['teamId'],
        'name': match_data['away']['name'],
        'country_name': match_data['away']['countryName'],
        'manager_name': match_data['away']['managerName'],
        'players': match_data['away']['players'],
    })
    return team_info

def get_match_info(match_data):
    return {
        'attendance': match_data['attendance'],
        'venue_name': match_data['venue_name'],
        'referee': match_data['referee'],
        'start_date': match_data['start_date'],  
        'start_time': match_data['start_time'],  
        'score': match_data['score'],
        'ht_score': match_data['ht_score'],
        'home_team_id': match_data['home_team_id'],
        'away_team_id': match_data['away_team_id'],
        'home_formations': match_data['home_formations'],
        'away_formations': match_data['away_formations']
    }

def insert_match(match_data, supabase):
    match_info = get_match_info()
    
    inserted_match = supabase.table('matches').insert(match_info).execute()
    
    if inserted_match.data:
        generated_match_id = inserted_match.data[0]['match_id']
        return generated_match_id
    else:
        return None
    
def insert_match_events(df, match_id, supabase):
    events = []
    for record in df.to_dict(orient='records'):
        event = MatchEvent(**record).dict()
        event['match_id'] = match_id
        events.append(event)
    
    execution = supabase.table('match_events').upsert(events).execute()

def insert_players(team_info, supabase):
    players = []
    for team in team_info:
        for player in team['players']:
            players.append({
                'player_id': player['playerId'],
                'team_id': team['team_id'],
                'shirt_no': player['shirtNo'],
                'name': player['name'],
                'position': player['position'],
                'age': player['age'],
                'height': player['height'],
                'weight': player['weight']
            })
            
    execution = supabase.table('players').upsert(players).execute()

if __name__ == "__main__":
    main()