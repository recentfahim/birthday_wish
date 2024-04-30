from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from django.conf import settings
from celery.schedules import crontab
import random

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'birthday_wish.settings')

app = Celery('birthday_wish')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


app.conf.beat_schedule = {
    'test_sum_task': {
        'task': 'users.tasks.test_sum',
        'schedule': 600
    },
    'wish_user_task': {
        'task': 'users.tasks.wish_user',
        'schedule': crontab(hour=settings.BIRTHDAY_WISH_HOUR, minute=settings.BIRTHDAY_WISH_MINUTE)
    },
}
app.conf.timezone = 'Asia/Dhaka'