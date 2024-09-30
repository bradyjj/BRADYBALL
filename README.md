# ⚽ Welcome to BRADYBALL ⚽

BRADYBALL is a comprehensive football *soccer* data application that combines web scraping, cloud database management, API and web application capabilities to provide a powerful platform for soccer enthusiasts, analysts, and professionals.

## 🚀 Features

- **Web Scraper**: Automatically collects up-to-date soccer data from various online sources.
- **Cloud Database**: Stores and manages large volumes of football data efficiently in the cloud.
- **API Service**: Retrieves data from cloud database and forms JSON responses
- **Web Application**: Provides an intuitive interface to access, visualize, and analyze soccer data.

## 🛠️ Technologies

- Web Scraping: Python, Soccerdata (https://github.com/probberechts/soccerdata)
- Cloud Database: Supabase PostgreSQL Database
- Web Application: AngularJS and D3.js
- Microservices: Celery, Redis, Docker

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

5. Run the API service:
   ```
   python -m uvicorn src.api.main:app --reload
   ```
   This command starts the server with auto-reload enabled, which is useful for development.


6. To start microservices:

   a. Ensure Docker and Docker Compose are installed on your system.

   b. Navigate to the directory containing your docker-compose.yml file.

   c. Start all services using Docker Compose:
   ```
   docker-compose up --build
   ```
   This command will build (if necessary) and start all the services defined in your docker-compose.yml file, including Redis, the Celery workers for different scraping tasks, Celery beat, and the Flower monitoring tool.

7. Access the Flower dashboard for monitoring Celery tasks:
   Open a web browser and go to http://localhost:5555

   Note: Make sure you have Python 3.7+, Docker, and Docker Compose installed on your system before starting. If you encounter any issues, ensure that all required files (docker-compose.yml, Dockerfile.service) are in the correct locations and that your project structure matches the paths specified in these files.

## 📃 API Docs

- http://127.0.0.1:8000/docs#/

## 🛠️ Microservices Architecture

BRADYBALL uses a microservices architecture for efficient data scraping and processing. The microservices are implemented using Celery with Redis as the message broker. Here's a brief overview:

- **Redis**: Acts as a message broker for the Celery tasks.
- **Celery Workers**: Separate workers for fbref, sofascore, transfermarkt, and whoscored data scraping.
- **Celery Beat**: Schedules periodic tasks for data updates.
- **Flower**: Provides a web-based monitoring interface for Celery tasks.

To interact with the microservices programmatically, you can use the Celery API in your Python code. For example:

```python
from microservices.fbref_service import example_task

# Run a task asynchronously
result = example_task.delay()

# Check the task status
print(f"Task ID: {result.id}")
print(f"Task Status: {result.status}")