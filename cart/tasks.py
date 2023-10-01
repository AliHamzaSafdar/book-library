from __future__ import absolute_import, unicode_literals
from celery import shared_task
from django.core.mail import send_mail


@shared_task(bind=True)
def send_receipt(self, email):
    print("Sending")
    send_mail("Receipt",
              "Receipt for Books and their Prices",
              "hammadhudhy@outlook.com",
              [email],
              fail_silently=False)
    print("Sent")
    return "Done"