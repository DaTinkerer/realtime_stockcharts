from django.urls import path
from .consumers import TimeSeriesConsumer, SymbolConsumer

ws_urlpatterns = [
    
    path('ws/time_series/', TimeSeriesConsumer.as_asgi()),
    
]