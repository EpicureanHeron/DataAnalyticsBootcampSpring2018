console.log(data);
// YOUR CODE HERE

var greek_x = data.map(data => data.pair);
var greek_y = data.map(data => data.greekSearchResults);
var roman_x = data.map(data => data.pair);
var roman_y = data.map(data => data.romanSearchResults);

var trace1 = {
  x: greek_x,
  y: greek_y,
  name: 'Greek God/Goddess',
  text: data.map(data => data.greekName),
  type: "bar"
}

var trace2 = {
  x: roman_x,
  y: roman_y,
  name: 'Roman God/Goddess',
  text: data.map(data => data.romanName),
  type: "bar"
}

var data = [trace1, trace2]

var layout = {
  title: "Romans vs Greeks",
  xaxis: {title: "God/Goddess Name"},
  yaxis: {title: "# of Searches"},
  barmode: 'group'
}

Plotly.newPlot("plot", data, layout);
