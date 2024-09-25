from celery import Celery

app = Celery('BRADYBALL',
             broker='redis://redis:6379/0',
             include=['microservices.fbref_service.tasks',
                      'microservices.sofascore_service.tasks',
                      'microservices.transfermarkt_service.tasks',
                      'microservices.whoscored_service.tasks'])

# Import schedules from each service
from microservices.fbref_service.tasks import schedule as fbref_schedule
from microservices.sofascore_service.tasks import schedule as sofascore_schedule
from microservices.transfermarkt_service.tasks import schedule as transfermarkt_schedule
from microservices.whoscored_service.tasks import schedule as whoscored_schedule

app.conf.beat_schedule = {}
app.conf.beat_schedule.update(fbref_schedule)
app.conf.beat_schedule.update(sofascore_schedule)
app.conf.beat_schedule.update(transfermarkt_schedule)
app.conf.beat_schedule.update(whoscored_schedule)