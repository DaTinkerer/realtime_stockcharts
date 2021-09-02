import django
django.setup()
import os
from celery import Celery
from django.contrib.sessions.models import Session

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'stockwatch.settings')

app = Celery('stockwatch')
app.config_from_object('django.conf:settings', namespace='CELERY')

# # s = Session.objects.get()
# sym = s.get_decoded()['sym']

app.conf.beat_schedule = {
    
    'get_time_series_data': {
        'task': 'stock_info.tasks.get_time_series_data',
        'schedule': 300.0,
        # 'args': sym
        
        
    },

}

app.autodiscover_tasks()