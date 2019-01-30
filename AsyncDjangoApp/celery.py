from __future__ import absolute_import
import os
from celery import Celery
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'AsyncDjangoApp.settings')

app = Celery('AsyncApp')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

# celery -A FlexitiApp worker -l info
# # rabbitmq-server