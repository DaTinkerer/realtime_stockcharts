For this project, I wanted to learn how to use Celery and Django Channels. I used Celery to fetch time series data from the Twelve Data finance api which Django 
Channels then recieves and sends to the front end in the form of candlestick charts. The charts were plotted using plotly.js. I used Celery beat to periodically call the celery task so that the data is updated automatically.
