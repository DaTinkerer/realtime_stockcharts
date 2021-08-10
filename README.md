This project displays time series stock information data in the form of candlestick charts. It uses Celery and Celery Beat to periodically send requests to the Twelve Data finance api and then sends the data to a Django Channels layer. Redis is used as the channel layer which stores the messages from the Celery task. Channels then sends the messages via websocket to the template where data is plotted using Plotly.js.

![](../screenshots/amd_chart.png?raw=true "AMD candlestick")
