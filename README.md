# ⚽ Welcome to BRADYBALL ⚽

<img width="441" alt="Screenshot 2025-02-28 at 10 10 35 PM" src="https://github.com/user-attachments/assets/08daab74-f958-432a-ab7e-883b20d1d3f0" />
<img alt="Second image" src="https://github.com/user-attachments/assets/9f0c817e-411f-467b-b1fb-34c735053d49" />


BRADYBALL is a comprehensive fooball *soccer* data application that combines web scraping, cloud database management, api and web application capabilities to provide a powerful platform for soccer enthusiasts, analysts, and professionals.

## 🚀 Features

- **Web Scraper**: Automatically collects up-to-date soccer data from various online sources.
- **Cloud Database**: Stores and manages large volumes of football data efficiently in the cloud.
- **API Service**: Retrieves data from cloud database and forms JSON responses
- **Web Application**: Provides an intuitive interface to access, visualize, and analyze soccer data.

## 🛠️ Technologies

- Web Scraping: Python, Soccerdata (https://github.com/probberechts/soccerdata)
- Cloud Database: Supabase PostgresSQL Database
- Web Application: AngularJS and D3.js

## 🎯 Purpose

BRADYBALL aims to democratize access to soccer data, enabling fans, coaches, and analysts to gain deeper insights into the beautiful game. Whether you're looking to track player performance, analyze team strategies, or simply explore historical soccer statistics, BRADYBALL provides the tools and data you need.

## 🌟 Why BRADYBALL?

- **Comprehensive Data**: From player stats to match results, BRADYBALL covers all aspects of soccer.
- **Real-time Updates**: Stay current with the latest soccer data through our efficient web scraper.
- **User-friendly Interface**: Access complex data sets with ease through our intuitive web application.
- **Scalable Architecture**: Built on cloud technology to handle growing data needs.

Get started with BRADYBALL and transform the way you interact with soccer data!

## 🏃‍♂️ To Run

1. Clone the repository:
   ```
   git clone https://github.com/bradyjj/BRADYBALL.git
   cd BRADYBALL
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   ```

3. Activate the virtual environment:
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS and Linux:
     ```
     source venv/bin/activate
     ```

4. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

5. Run the application:
   ```
   python -m uvicorn src.api.main:app --reload
   ```

   This command starts the server with auto-reload enabled, which is useful for development.

Note: Make sure you have Python 3.7+ installed on your system before starting.

## 📃 API Docs

- http://127.0.0.1:8000/docs#/
