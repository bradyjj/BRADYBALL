# Leagues
ENG_PREMIER_LEAGUE = 'ENG-Premier League'
ESP_LA_LIGA = 'ESP-La Liga'
FRA_LIGUE_1 = 'FRA-Ligue 1'
GER_BUNDESLIGA = 'GER-Bundesliga'
ITA_SERIE_A = 'ITA-Serie A'

WHOSCORED_URL_TO_CONST = {
    'England-Premier-League': ENG_PREMIER_LEAGUE,
    'Spain-LaLiga': ESP_LA_LIGA,
    'France-Ligue-1': FRA_LIGUE_1,
    'Germany-Bundesliga': GER_BUNDESLIGA,
    'Italy-Serie-A': ITA_SERIE_A
}

# WHOSCORED URLs
WHOSCORED_URL = "https://www.whoscored.com"
WHOSCORED_MATCH_URL_TEMPLATE = "https://www.whoscored.com/Matches/{match_id}/{page}/{league}-{season}-{teams}"

# TRANSFERMARKT URLs
TRANSFERMARKT_PLAYER_URL = "https://www.transfermarkt.us/{player_name}/profil/spieler/{player_id}"
TRANSFERMARKT_TEAM_STAFF_URL = "https://www.transfermarkt.us/ceapi/staff/team/{team_id}/?saison_id={season_year}&wettbewerb_id={transfermarkt_league_id}"
TRANSFERMARKT_TRANSFER_HISTORY_URL = "https://www.transfermarkt.us/ceapi/transferHistory/list/{player_id}"
TRANSFERMARKT_MARKET_VALUE_URL = "https://www.transfermarkt.us/ceapi/marketValueDevelopment/graph/{player_id}"
TRANSFERMARKT_COUNTRY_URL = "https://www.transfermarkt.us/wettbewerbe/national/wettbewerbe/{country_id}/saison_id/{year}"
TRANSFERMARKT_COUNTRY_IDS = {
    "England": "189",
    "France": "50",
    "Spain": "157",
    "Germany": "40",
    "Italy": "75"
}

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}
