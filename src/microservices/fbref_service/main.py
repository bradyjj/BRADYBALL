from common.celery.celery_app import app
from microservices.fbref_service.tasks import *

if __name__ == '__main__':
    scrape_fbref_data.delay()