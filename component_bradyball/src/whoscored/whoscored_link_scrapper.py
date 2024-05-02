import soccerdata as sd
import os
import pandas as pd

# Define the directory for saving schedules
schedules_dir = 'schedules'
os.makedirs(schedules_dir, exist_ok=True)

# Specify the leagues and seasons you are interested in
leagues = ['ENG-Premier League', 'ESP-La Liga', 'FRA-Ligue 1', 'GER-Bundesliga', 'ITA-Serie A']

start_year = 1999
end_year = 2023
seasons = [f"{year}/{year+1}" for year in range(start_year, end_year + 1)]

ws = sd.WhoScored(leagues='ITA-Serie A', seasons=seasons, no_cache=True)

try:
    # Fetch the schedule
    schedule = ws.read_schedule()
    print("Fetched schedule:", schedule)

    # Convert the schedule to a DataFrame
    df = pd.DataFrame(schedule) 

    # Create a filename and save path
    filename = "ITA-schedules.csv"
    filepath = os.path.join(schedules_dir, filename)

    # Save the DataFrame to CSV
    df.to_csv(filepath, index=False)
    print(f"Saved schedule to {filepath}")
except Exception as e:
    print(f"Error during processing: {e}")
