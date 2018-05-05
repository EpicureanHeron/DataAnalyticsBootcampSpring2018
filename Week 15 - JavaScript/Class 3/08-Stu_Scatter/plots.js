console.log(data);
// YOUR CODE HERE

// var high_jump = data.map(data => data.high_jump);
// var discus_throw = data.map(data => data.discus_throw);
// var long_jump = data.map(data => data.long_jump);
// var year = data.map(data => data.year);
console.log(data.high_jump);

var trace1 = {
  x: data.year,
  y: data.high_jump,
  name: 'High Jump',
  mode: "markers",
  type: "scatter",
  marker: {
    color: 'blue'
  }
}

var trace2 = {
  x: data.year,
  y: data.discus_throw,
  name: 'Discus Throw',
  mode: "markers",
  type: "scatter",
  marker: {
    color: 'green'
  }
}

var trace3 = {
  x: data.year,
  y: data.long_jump,
  name: 'Long Jumps',
  mode: "markers",
  type: "scatter",
  marker: {
    color: 'red'
  }
}

var data = [trace1, trace2, trace3]

var layout = {
  title: "Olympic Results",
  xaxis: {title: "Year"},
  yaxis: {title: "Result (inches)"}
}

Plotly.newPlot("plot", data, layout);
