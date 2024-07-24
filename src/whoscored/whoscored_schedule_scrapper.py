import soccerdata as sd
import os
import pandas as pd

# Define the directory for saving schedules
schedules_dir = 'schedules'
os.makedirs(schedules_dir, exist_ok=True)

# Specify the leagues and seasons you are interested in
leagues = ['ENG-Premier League', 'ESP-La Liga', 'FRA-Ligue 1', 'GER-Bundesliga', 'ITA-Serie A']

start_year = 2024
end_year = 2025
season = "2024/2025"
seasons = [f"{year}/{year+1}" for year in range(start_year, end_year + 1)]

ws = sd.WhoScored(leagues=leagues, seasons=season, no_cache=True)

try:
    # Fetch the schedule
    schedule = ws.read_schedule()
    print("Fetched schedule:", schedule)
    
    for league in leagues:
        for season in seasons:
            # Filter the schedule for the current league and season
            filtered_schedule = [match for match in schedule if match['league'] == league and match['season'] == season]

            # Convert the filtered schedule to a DataFrame
            df = pd.DataFrame(filtered_schedule)

            # Create a filename and save path
            filename = f"{league}-{season}-schedule.csv"
            filepath = os.path.join(schedules_dir, filename)

            # Save the DataFrame to CSV
            df.to_csv(filepath, index=False)
            print(f"Saved schedule for {league} {season} to {filepath}")

except Exception as e:
    print(f"Error during processing: {e}")