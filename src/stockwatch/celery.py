import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'stockwatch.settings')

app = Celery('stockwatch')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.beat_schedule = {
    
    'get_time_series_data': {
        'task': 'stock_info.tasks.get_time_series_data',
        'schedule': 300.0
    },

}

app.autodiscover_tasks()