from __future__ import absolute_import
from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_welcome_mail(to_email):
    send_mail(
        'you have signed up on blogging app ',
        'welcome to blogging app ',
        'admin@example.com',
        [to_email],
        fail_silently=False
    )
