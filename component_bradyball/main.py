from datetime import datetime
from src.whoscored.whoscored_schedule_upload import load_whoscored_schedules
from src.transfermarkt.transfermarkt import scrape_transfermarkt_player_data

def main():
    while True:
        print("Please choose an option:")
        print("1. Load WhoScored Schedules")
        print("2. Scrape Transfermarkt Player Data")
        print("3. Exit")
        choice = input("Enter your choice (1, 2, or 3): ")
        
        if choice == '1':
            print("Loading WhoScored Schedules...")
            load_whoscored_schedules()
        elif choice == '2':
            current_season = datetime.now().year-1
            print(f"Scraping Transfermarkt Player Data for the season starting in {current_season}...")
            scrape_transfermarkt_player_data(current_season)
        elif choice == '3':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()