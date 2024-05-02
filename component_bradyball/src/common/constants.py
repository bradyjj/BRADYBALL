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

# URLs
WHOSCORED_URL = "https://www.whoscored.com"
WHOSCORED_MATCH_URL_TEMPLATE = "https://www.whoscored.com/Matches/{match_id}/Live/{league}-{season}-{teams}"