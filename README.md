This project fetches time series stock market data from the Twelve Data finance api. Data is fetched using a background task queue. The task queue then sends the data to a websocket server which will then send data to the client. In the client, the time series information is illustrated with candlestick charts.

Technologies used:
- Django
- Django Channels (websockets)
- Celery (task queue)
- Redis (channel layer used as a backing store for communication between celery tasks and Django Channels)
- Plotly.js (for drawing candlestick charts)
- Twelve Data api


![](../screenshots/amd_chart.png?raw=true "AMD candlestick")
