This project fetches time series stock market data from the Twelve Data finance api. Data is fetched using a background task queue. The task queue then sends the data to a websocket server which will then send data to the client. In the client, the time series information is illustrated with candlestick charts.

![](../screenshots/amd_chart.png?raw=true "AMD candlestick")
