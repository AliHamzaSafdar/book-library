from __future__ import absolute_import, unicode_literals
from celery import shared_task
from django.core.mail import send_mail


@shared_task(bind=True)
def send_receipt(self):
    print("Sending")
    send_mail("Receipt",
              "Books and Prices",
              "hammadhudhy@outlook.com",
              ["hammadhudhy@gmail.com"],
              fail_silently=False)
    print("Sent")
    return "Done"