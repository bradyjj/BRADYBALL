import re
import requests
import traceback

import pandas as pd
import numpy as np

from typing import List
from tqdm import tqdm
from bs4 import BeautifulSoup
from pydantic import ValidationError
from supabase import create_client

from src.common.pydantic_models import TransfermarktPlayer
from src.common.constants import HEADERS, TRANSFERMARKT_COUNTRY_IDS, TRANSFERMARKT_COUNTRY_URL, TRANSFERMARKT_MARKET_VALUE_URL, TRANSFERMARKT_TRANSFER_HISTORY_URL
from src.common.config import SUPABASE_URL, SUPABASE_KEY
    
def scrape_transfermarkt_player_data(year): 
    supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

    for country, country_id in TRANSFERMARKT_COUNTRY_IDS.items():
        country_url = TRANSFERMARKT_COUNTRY_URL.format(country_id=country_id, year=year)
        print(f"Scraping transfermarkt player data for {country}...")
        player_df = scrape_country_competitions(country_url)
        new_rows = []
        
        for index, row in player_df.iterrows():
            detailed_df = get_detailed_player_data(row['url'])
            
            # Update the row with new columns
            for col in detailed_df.columns:
                row[col] = detailed_df.loc[0, col]
            new_rows.append(row)

        # Convert the list of updated rows back to a DataFrame
        updated_player_df = pd.DataFrame(new_rows)
        filename = f'{country}-{country_id}-{year}.csv'
        updated_player_df.to_csv(filename, index=False)  
              
        # Match df to pydantic model and upload to db
        player_models = [TransfermarktPlayer(**row).dict() for index, row in updated_player_df.iterrows()]
        print(f"Uploading transfermarkt player data for {country} to db...")
        upload_to_db(supabase, player_models)

def upload_to_db(supabase, data):
    batch_size = 50
    for i in range(0, len(data), batch_size):
        batch_data = data[i:i+batch_size]
        validated_data = []
        for row in batch_data:
            try:
                transfermarkt_player = TransfermarktPlayer(**row)
                validated_data.append(transfermarkt_player.dict())
                print(f"Uploading row: {transfermarkt_player}")
            except ValidationError as e:
                print(f"\nError validating data in batch {i//batch_size + 1}: {e}")
                continue

        if validated_data:
            try:
                response = supabase.table('transfermarkt_player').insert(validated_data).execute()
            except Exception as e:
                traceback_details = traceback.format_exc()
                print(f"\nException during upload of batch {i//batch_size + 1}: {traceback_details}")
        else:
            print(f"\nNo valid data to upload in batch {i//batch_size + 1}.")
            
def scrape_country_competitions(country_url):
    soup = fetch_competition_data(country_url)
    competitions = extract_competitions(soup)
    all_player_data = []

    for competition in tqdm(competitions, desc="Competitions"):
        comp_soup = fetch_competition_data(competition['url'])
        teams = extract_teams(comp_soup, competition['url'])
        for team in teams:
            team_soup = fetch_players(team)
            players = extract_player_details(team_soup, competition['name'], team['team_name'])
            all_player_data.extend(players)

    player_df = pd.DataFrame(all_player_data)
    # Replace empty strings with NaN and then drop rows where 'player_name' is NaN
    player_df['player_name'] = player_df['player_name'].replace('', np.nan)
    player_df.dropna(subset=['player_name'], inplace=True)
    return player_df

def fetch_competition_data(url):
    response = requests.get(url, headers=HEADERS)
    return BeautifulSoup(response.content, "html.parser")

def extract_competitions(soup):
    competitions = []
    competition_table = soup.find('table', class_='items')
    for row in competition_table.find_all('tr'):
        header = row.find('td', class_='extrarow')
        if header and 'First Tier' in header.text:
            links = row.find_next_sibling('tr').find_all('a', href=True, title=True)
            for link in links:
                if 'wettbewerb' in link['href']:
                    competitions.append({
                        'name': link.get_text(strip=True),
                        'url': f"https://www.transfermarkt.us{link['href']}"
                    })
    return competitions

def extract_teams(soup, competition_url):
    teams_data = []
    table = soup.find('table', class_='items')
    rows = table.find_all('tr', class_=['odd', 'even'])
    
    for row in rows:
        team_link = row.find('td', class_='hauptlink no-border-links').find('a', href=True)
        if team_link:
            team_name = team_link.text.strip()  # Extracting team name
            team_id = team_link['href'].split('/')[4]
            team_url = team_link['href'].rsplit('/', 1)[0]

            teams_data.append({
                "team_name": team_name,
                "team_id": team_id,
                "team_url": team_url,
                "transfermarkt_league_id": competition_url.split('/')[-1]
            })
        
    print_team_data(teams_data)
    return teams_data

def fetch_players(team):
    team_url = f"https://www.transfermarkt.us{team['team_url']}/kader/verein/{team['team_id']}/saison_id/2023/plus/1"
    response = requests.get(team_url, headers=HEADERS)
    return BeautifulSoup(response.content, "html.parser")

def print_team_data(teams_data):
    for team in teams_data:
        print(f"Team: {team['team_name']}")
        print(f"Team ID: {team['team_id']}")
        print(f"League ID: {team['transfermarkt_league_id']}")
        print(f"URL: {team['team_url']}")
        print("-" * 40)

def print_player_data(all_player_data):
    for player in all_player_data:
        print(f"Competition: {player['competition_name']}")
        print(f"Team: {player['team_name']}")
        print(f"Player Name: {player['player_name']}")
        print(f"Position: {player['position']}")
        print(f"URL: {player['url']}")
        print("-" * 40)

def extract_player_details(soup, competition_name, team_name):
    all_player_data = []
    players = soup.find_all('tr', class_=['odd', 'even'])

    for player in players:
        # Find the 'a' tag within the cell that has class 'hauptlink', which should contain the player's name
        name_tag = player.find('td', class_='hauptlink').find('a', href=True)
        if name_tag:
            name = name_tag.text.strip()
            player_url = "https://www.transfermarkt.us" + name_tag['href']

            # To find the position, navigate to the sibling 'tr' of the 'tr' containing the player's name tag
            position_tag = player.find('td', class_='posrela').find('tr').find_next_sibling('tr')
            if position_tag and position_tag.find('td'):
                position = position_tag.find('td').text.strip()
            else:
                position = 'Position Not Found'

            all_player_data.append({
                'competition_name': competition_name,
                'team_name': team_name,
                'player_name': name,
                'position': position,
                'url': player_url
            })

    print_player_data(all_player_data)
    return all_player_data

def get_detailed_player_data(url):
    # Get player id from url
    player_id = url.split('/')[-1]

    # Make request to webpage
    response = requests.get(url, headers=HEADERS)

    # Create soup and parse html
    soup = BeautifulSoup(response.content, "html.parser")
    
    try:
        # Use css selectors to find class and then get text, remove whitespace, remove null
        player_name = soup.select_one('h1[class="data-header__headline-wrapper"]').text.split('\n')[-1].strip()
    except AttributeError:
        player_name = None

    try:
        # Use css selectors to find class and then get text, remove #, remove null
        player_number = soup.select_one('span[class="data-header__shirt-number"]').text.replace('#', '').strip()
    except AttributeError:
        player_number = None

    try:
        player_contract_expiry = re.search(r"Contract expires: .*__content\">(.*?)</span>", str(soup)).group(1)
        if player_contract_expiry == "-":
            player_contract_expiry = None
    except AttributeError:
        player_contract_expiry = None

    try:
        player_foot = re.search(r"Foot:</span>\s*<span class=\"info-table__content info-table__content--bold\">(.*?)</span>", str(soup)).group(1)
    except AttributeError:
        player_foot = None

    try:
        player_agent = re.search(r"Player agent:</span>\s*<span[^>]*>\s*<a[^>]*>([^<]+)</a>", str(soup)).group(1)
    except AttributeError:
        player_agent = None

    try:
        player_outfitter = re.search(r"Outfitter:</span>\s*<span class=\"info-table__content info-table__content--bold\">\s*(.*?)\s*</span>", str(soup)).group(1)
    except AttributeError:
        player_outfitter = None

    try:
        player_citizenship = re.search(r"Citizenship:</span>[\s\S]*?alt=\"([^\"]+)\"", str(soup)).group(1)
    except AttributeError:
        player_citizenship = None

    try:
        player_contract_start = re.search(r"Joined:</span>\s*<span[^>]*>\s*([^<]+)</span>", str(soup)).group(1)
        if player_contract_start == "-":
            player_contract_start = None
    except AttributeError:
        player_contract_start = None
        
    try:
        # Extract the date of birth and age
        dob_and_age = re.search(r"Date of birth/Age:</span>\s*<span[^>]*>\s*<a[^>]*>([^<]+)\s*\((\d+)\)</a>", str(soup))
        date_of_birth = dob_and_age.group(1)
        age = dob_and_age.group(2)
    except AttributeError:
        date_of_birth = None
        age = None

    try:
        # Find the span that directly contains birthplace
        birthplace_span = soup.find('span', itemprop="birthPlace")
        if birthplace_span:
            city = birthplace_span.text.strip()
            country_img = birthplace_span.find_previous('img', class_="flaggenrahmen")
            if country_img and country_img.has_attr('title'):
                country = country_img['title'].strip()
                player_birthplace = f"{city}, {country}"
            else:
                # If no country, just leave as city
                player_birthplace = city
        else:
            player_birthplace = None
    except AttributeError:
        player_birthplace = None

    # Organize data into a dictionary
    player_data = {
        'player_id': player_id,
        'player_name': player_name,
        'shirt_no': player_number,
        'contract_expiry_date': player_contract_expiry,
        'foot': player_foot,
        'agent': player_agent,
        'outfitter': player_outfitter,
        'citizenship': player_citizenship,
        'contract_start_date': player_contract_start,
        'date_of_birth': date_of_birth,
        'age': age,
        'birthplace': player_birthplace
    }
    
    # Get API data
    market_values_json = get_market_value_data(player_id)
    transfer_histories_json = get_transfer_history_data(player_id)

    player_df = pd.DataFrame([player_data])

    # Serialize list of dicts to JSON string and assign directly to DataFrame column
    player_df['market_value'] = [market_values_json]
    player_df['transfer_history'] = [transfer_histories_json]

    print(player_df)
    return player_df

def get_market_value_data(player_id):
    market_value_url = TRANSFERMARKT_MARKET_VALUE_URL.format(player_id=player_id)
    market_value_response = requests.get(market_value_url, headers=HEADERS)
    market_value_data = market_value_response.json()

    # Extract only the columns you need from the JSON response
    market_values = []
    for entry in market_value_data['list']:
        market_value = {
            'age': entry['age'],
            'team_name': entry['verein'],
            'date': entry['datum_mw'],
            'market_value': entry['mw']
        }
        market_values.append(market_value)

    return market_values

def get_transfer_history_data(player_id):
    transfer_history_url = TRANSFERMARKT_TRANSFER_HISTORY_URL.format(player_id=player_id)
    transfer_history_response = requests.get(transfer_history_url, headers=HEADERS)
    transfer_history_data = transfer_history_response.json()

    # Extract the list of data points needed
    transfer_history_list = transfer_history_data.get('transfers', [])

    transfers_histories = []
    for transfer in transfer_history_list:
        simplified_transfer = {
            'date': transfer['dateUnformatted'],
            'season': transfer['season'],
            'market_value': transfer['marketValue'],
            'transfer_fee': transfer['fee'],
            'from_club_name': transfer['from']['clubName'],
            'to_club_name': transfer['to']['clubName']
        }
        transfers_histories.append(simplified_transfer)

    return transfers_histories