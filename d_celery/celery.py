import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'd_celery.settings')

app = Celery('d_celery')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

# celery beat task
# app.conf.beat_schedule = {
#     'send-spam-every-10-minute': {
#         'task': 'main.tasks.send_beat_email',
#         'schedule': crontab(minute='*/10'),
#     }
# }
