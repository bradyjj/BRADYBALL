# component_bradyball/main.py
from src.whoscored import whoscored_scraped, whoscored_clean_data, whoscored_upload_to_db

def main():
    # Scrape data from WhoScored
    raw_data = whoscored_scraped()
    cleaned_data = whoscored_clean_data(raw_data)
    whoscored_upload_to_db(cleaned_data)

    print("Data scraping, cleaning, and uploading complete.")

if __name__ == "__main__":
    main()
