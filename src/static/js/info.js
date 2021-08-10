// get message from channels
const socket = new WebSocket('ws://localhost:8000/ws/time_series/');
socket.onmessage = function(event){

  // const data is the dictionary with
  // all the channels messages
  const data = JSON.parse(event.data);

  const trace = {

    x: data.date,
    open: data.open,
    high: data.high,
    close: data.close,
    low: data.low,

    increasing: {
      line: {color: '#99ccff'}
    },
    decreasing: {
      line: {color: '#8c8c8c'},
      
      
    },

    type: 'candlestick',
    xaxis: 'x',
    yaxis: 'y',
    
  };

  const d = [trace];
  
  const layout = {
    title: {text: data.symbol + ' | ' + '$' + data.price + ' | ' + data.exchange },
    yaxis: {title: 'Price (USD)'},
    width: 1300,
    height: 800,
    dragmode: 'zoom',
    showlegend: false,
    xaxis: {
      rangeslider: {
                  visible: false
          },
      title: 'Date',
    
    },
    plot_bgcolor: '#414863',
    paper_bgcolor: '#414863',
    font: {'color': "#fff", 'family': "'Lato', sans-serif"}
    
  };
  
  Plotly.newPlot('chart', d, layout);
  

}