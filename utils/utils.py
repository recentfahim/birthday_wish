from django.core.mail import send_mail
import os
from datetime import datetime
from django.conf import settings
import random
import logging

logger = logging.getLogger(__name__)


def email_send(email, subject=None, body=None):
    if subject and body and email:
        send_mail(subject, body, settings.SEND_EMAIL_FROM, [email, ])
        return True

    return False

def email_save_local(email, content):
    filename = f"sent_emails/{email}_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt"
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, 'w') as file:
        file.write(content)


def send_birthday_wish_email(user=None):
    if user.email:
        subject = f'Happy Birthday ' + user.first_name if user.first_name else ''
        body = 'Dear ' + user.first_name if user.first_name else '' + '\n' + 'Happy Birthday to you and Many many happy returns of the day.\n' + 'Team Friends Corp.'
        try:
            if settings.SEND_REAL_EMAIL:
                logger.info(f'Sending email to {user.email}...')
                email_send(user.email, subject, body)
                logger.info(f'Birthday email sent to {user.email} successfully!')
                return True
            else:
                if settings.SAVE_EMAIL_LOCAL:
                    logger.info(f'Saving email sending to {user.email} to local...')
                    email_save_local(user.email, body)
                    logger.info(f'Saving birthday email sent to {user.email} successfully!')
                    return True
                else:
                    logger.info(f'Fake sending email to {user.email}...')
                    logger.info(f'Birthday email fake sent to {user.email} successfully!')
                    return True
        except Exception as e:
            logger.error(f'Failed to send birthday email to {user.email}: {str(e)}')
            return False
    else:
        logger.error('Failed to send birthday email because email does not exist for the user')
        return False


def add_test():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    result = num1 + num2

    return f'Sum of {num1} and {num2} is {result}'