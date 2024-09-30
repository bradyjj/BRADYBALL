from celery import Celery

app = Celery('BRADYBALL',
             broker='redis://redis:6379/0',
             backend='redis://redis:6379/0',
             include=['microservices.fbref_service.tasks',
                      'microservices.sofascore_service.tasks',
                      'microservices.transfermarkt_service.tasks',
                      'microservices.whoscored_service.tasks'])
