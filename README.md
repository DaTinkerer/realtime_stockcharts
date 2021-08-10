This project displays time series stock information data in the form of candlestick charts. It uses Celery and Celery Beat to periodically send requests to the Twelve Data finance api and then sends the data to a Django Channels layer. Redis is used as the channel layer which makes it possible to commucate with the Celery task messages. Channels then sends the data via websocket to the front end where the time series data is plotted using Plotly.js.

![](../screenshots/amd_chart.png?raw=true "AMD candlestick")
