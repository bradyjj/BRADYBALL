from datetime import datetime
from src.whoscored.whoscored_schedule_upload import load_whoscored_schedules
from src.transfermarkt.transfermarkt import scrape_transfermarkt_player_data
from src.fbref.fbref import scrape_fbref_data

def main():
    while True:
        print("Please choose an option:")
        print("1. Load WhoScored Schedules")
        print("2. Scrape Transfermarkt Player Data")
        print("3. Scrape Fbref Team Season Stats")
        print("4. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            print("Loading WhoScored Schedules...")
            load_whoscored_schedules()
        elif choice == '2':
            current_season = datetime.now().year-1
            print(f"Scraping Transfermarkt Player Data for the season starting in {current_season}...")
            scrape_transfermarkt_player_data(current_season)
        elif choice == '3':
            print(f"Scraping Fbref Team Season Stats for the season...")
            scrape_fbref_data()
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()