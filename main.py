from datetime import datetime
from src.whoscored.whoscored_schedule_upload import load_whoscored_schedules
from src.transfermarkt.transfermarkt import scrape_transfermarkt_player_data
from src.fbref.fbref_team import scrape_fbref_team_data
from src.fbref.fbref_player import scrape_fbref_player_data

START_SEASON = '2223'
END_SEASON = '2223'


def generate_season_list():
    start_century = int(START_SEASON[:2])
    end_century = int(END_SEASON[:2])

    start_year = 1900 + start_century
    end_year = 2000 + end_century + 1

    seasons = []
    for year in range(start_year, end_year):
        next_year = year + 1
        season = f'{year % 100:02d}{next_year % 100:02d}'
        seasons.append(season)

    return seasons


def main():
    while True:
        print("\nPlease choose an option:")
        print("1. Load WhoScored Schedules")
        print("2. Scrape Transfermarkt Player Data")
        print("3. Scrape Fbref Team Season Stats")
        print("4. Scrape Fbref Player Season Stats")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            print("Loading WhoScored Schedules...")
            load_whoscored_schedules()
        elif choice == '2':
            print(f"Scraping Transfermarkt Player Data for seasons {
                  START_SEASON}-{END_SEASON}...")
            for season in generate_season_list(START_SEASON, END_SEASON):
                scrape_transfermarkt_player_data(season)
        elif choice == '3':
            print(f"Scraping Fbref Team Season Stats for seasons {
                  START_SEASON}-{END_SEASON}...")
            scrape_fbref_team_data()
        elif choice == '4':
            print(f"Scraping Fbref Player Season Stats for seasons {
                  START_SEASON}-{END_SEASON}...")
            scrape_fbref_player_data()
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
