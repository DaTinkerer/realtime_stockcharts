from channels.generic.websocket import AsyncWebsocketConsumer, WebsocketConsumer
import json
from asgiref.sync import async_to_sync
from django.core.files import File
from .tasks import get_time_series_data

class TimeSeriesConsumer(AsyncWebsocketConsumer):
    # connect and disconnect to channels group
    async def connect(self):
        await self.channel_layer.group_add('time_series', self.channel_name)
        await self.accept()

    async def disconnect(self):
        await self.channel_layer.group_discard('time_series', self.channel_name)

    # get message from celery task
    async def send_time_series(self, event):
        date = event['date']
        open_price = event['open']
        high = event['high']
        close = event['close']
        low = event['low']
        symbol = event['symbol']
        price = event['price']
        exchange = event['exchange']
        
        # send message to front end
        await self.send(json.dumps({
            'date': date,
            'open': open_price,
            'high': high,
            'close': close,
            'low': low,
            'symbol': symbol,
            'price': price,
            'exchange': exchange,
        }))
        
class SymbolConsumer(WebsocketConsumer):
    def connect(self):
        async_to_sync(self.channel_layer.group_add)('symbol', self.channel_name)
    def disconnect(self):
        async_to_sync(self.channel_layer.group_discard)('symbol', self.channel_name)


    def receive(self, data):
        data_json = json.loads(data)
        symbol = data_json['symbol']

        with open('stock_info/temp.txt', 'w') as f:
            f.write(symbol)
            
            f.close
        get_time_series_data.delay()
    pass
