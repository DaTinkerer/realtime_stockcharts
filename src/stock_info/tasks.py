import requests
from celery import shared_task
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from django.core.files import File
import plotly.graph_objects as go
from plotly.offline import plot
import pandas as pd
import json
from stockwatch.secrets import api_key
channel_layer = get_channel_layer()
    
@shared_task()
def get_time_series_data ():
    
    with open('stock_info/temp.txt', 'r+') as f:
        f.seek(0)
        sym = f.read()
        f.close

        payload = {'symbol': sym}
        r = requests.get(f'https://api.twelvedata.com/time_series?&interval=4h&apikey={api_key}&outputsize=500', 
        params=payload)
        
        res = r.json()
        symbol = res['meta']['symbol']
        date = []
        open_price = []
        high = []
        close = []
        low = []
        for value in res['values']:
            date.append(value['datetime'])
            open_price.append(value['open'])
            high.append(value['high'])
            close.append(value['close'])
            low.append(value['low'])

    
        
        r2 = requests.get(f'https://api.twelvedata.com/price?apikey={api_key}&dp=2', 
        params=payload)
        res2 = r2.json()
        price = res2['price']

        # sends message to channels group
        async_to_sync(channel_layer.group_send)('time_series', {'type': 'send_time_series', 
        'date': date,
        'open': open_price,
        'high': high,
        'close': close,
        'low': low,
        'symbol': symbol,
        'price': price,
        })

     
    
            

    
    

        

    
    
    

    