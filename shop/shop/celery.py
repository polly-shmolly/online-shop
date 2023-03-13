import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "shop.settings")
app = Celery("shop")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'every-30-min': {
        'task': 'shop.tasks.get_products_statistic',
        'schedule': crontab(minute='*/30'),
    },
    'every-1-min': {
        'task': 'shop.tasks.get_producer_statistic',
        'schedule': crontab(),
    },
}
