This project displays time series stock data in the form of candlestick charts. It uses Celery and Celery Beat to periodically send requests to the Twelve Data 
finance api and then sends the data to a Django Channels group. Channels then sends the data via websocket to the front end where the time series data is
plotted using Plotly.js.
