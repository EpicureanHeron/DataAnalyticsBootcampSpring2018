// @TODO: Complete the following sections

console.log(data);
// Sort the data array using the greekSearchResults value
// var greek_name = data.map(data => data.greekName);
// var greek_y = data.map(data => data.greekSearchResults);

data.sort(function compareFunction(firstNum, secondNum) {
  return secondNum.greekSearchResults - firstNum.greekSearchResults;
});

// Slice the first 10 objects for plotting
const top_10 = data.slice(0, 10);
console.log(top_10);
top_10.reverse();

// Trace1 for the Greek Data
var trace1 = {
  x: top_10.map(data => data.greekSearchResults),
  y: top_10.map(data => data.greekName),
  name: 'Greek God/Goddess',
  type: "bar",
  orientation: 'h'
}
// set up the data variable
var data = [trace1];
// set up the layout variable
var layout = {
  title: "Romans vs Greeks",
  xaxis: {title: "# of Searches"},
  yaxis: {title: "God/Goddess Name"},
}
// Render the plot to the div tag with id "plot"
Plotly.newPlot("plot", data, layout);
