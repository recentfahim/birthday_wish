from celery import shared_task
from django.contrib.auth import get_user_model
from datetime import datetime
import logging
from utils.utils import send_birthday_wish_email, add_test

logger = logging.getLogger(__name__)


@shared_task
def test_sum():
    return add_test()


@shared_task
def wish_user():
    User = get_user_model()
    today = datetime.now()
    users = User.objects.filter(date_of_birth__day=today.day, date_of_birth__month=today.month)
    logger.info(f'Start sending Birthday email...')
    for user in users:
        send_birthday_wish_email(user)
    logger.info(f'End sending Birthday email...')

    return 'All birthday email sent successfully'