from channels.generic.websocket import AsyncWebsocketConsumer
import json

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
        
        # send message to front end
        await self.send(json.dumps({
            'date': date,
            'open': open_price,
            'high': high,
            'close': close,
            'low': low,
            'symbol': symbol,
            'price': price,
        }))
        