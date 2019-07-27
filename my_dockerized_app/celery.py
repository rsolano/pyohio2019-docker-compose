import os
from celery import Celery
from django.conf import settings

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'my_dockerized_app.settings')

app = Celery('my_dockerized_app')

app.conf.broker_url = "redis://redis:6379"
app.conf.result_backend = "redis://redis:6379"
app.conf.redis_max_connections = 10
app.conf.broker_pool_limit = None
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
