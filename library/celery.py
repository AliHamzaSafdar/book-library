from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'library.settings')
app = Celery('library')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.conf.broker_url = 'amqp://guest:guest@rabbitmq//'
app.conf.broker_transport_options = {'socket_timeout': 30}
app.autodiscover_tasks()


