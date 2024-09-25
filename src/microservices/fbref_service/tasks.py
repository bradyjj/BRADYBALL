from common.celery.celery_app import app

@app.task
def scrape_fbref_data():
    pass

schedule = {
    'scrape-fbref-data': {
        'task': 'microservices.fbref_service.tasks.scrape_fbref_data',
        'schedule': 604800.0,  # 7 days in seconds
    },
}