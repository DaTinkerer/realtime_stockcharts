const spinner = document.querySelector(".spinner");
const msg = document.querySelector(".message");
// get message from channels
const socket = new WebSocket("ws://localhost:8000/ws/time_series/");
socket.onmessage = (event) => {
  // const data is the dictionary with
  // all the channels messages
  const data = JSON.parse(event.data);
  console.log(data);

  const trace = {
    x: data.date,
    open: data.open,
    high: data.high,
    close: data.close,
    low: data.low,

    increasing: {
      line: { color: "#99ccff" },
    },
    decreasing: {
      line: { color: "#8c8c8c" },
    },

    type: "candlestick",
    xaxis: "x",
    yaxis: "y",
  };

  const d = [trace];

  const layout = {
    title: {
      text: data.symbol + " | " + "$" + data.price + " | " + data.exchange,
    },
    yaxis: { title: "Price (USD)" },
    width: 1300,
    height: 800,
    dragmode: "zoom",
    showlegend: false,
    xaxis: {
      rangeslider: {
        visible: false,
      },
      title: "Date",
    },
    plot_bgcolor: "#414863",
    paper_bgcolor: "#414863",
    font: { color: "#fff", family: "'Lato', sans-serif" },
  };
  const config = {responsive: true}
  spinner.style.display = "none";
  Plotly.newPlot("chart", d, layout, config);
  // stop the timer if there is a message
  clearTimeout(hideSpinner);
};
// I want to hide the spinner and display a message after some time
//if the chart doesn't show. probably means
// stock symbol isn't available on my free api plan.
let hideSpinner = setTimeout(() => {
  spinner.style.display = "none";
  msg.style.display = "block";
}, 7000);

window.addEventListener("load", () => {
  hideSpinner;
});
