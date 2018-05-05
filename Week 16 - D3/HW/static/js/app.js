// populate option dropdown
Plotly.d3.json("/names", function(error, response) {
  console.log(response);
  $select = document.getElementById('selDataset')

  for (var i = 0; i < response.length; i++) {
    var option = document.createElement("option");
    option.value = response[i];
    option.innerHTML = response[i]

    $select.appendChild(option);
  }

});

// create default pie chart
// TODO: figure out how to get data from two urls for same plot
Plotly.d3.json("/samples/BB_940", function(error, response) {
  if (error) return console.warn(error);
  top_otu = response[0].otu_id.slice(0,9);
  top_values = response[0].value.slice(0,9);
  console.log(top_otu);
  console.log(top_values);
  data = [{
    "labels": top_otu,
    "values": top_values,
    "type": "pie"
  }];
  var PIE = document.getElementById('pie');
  Plotly.newPlot(PIE, data);
})

// create default bubble chart
// TODO: figure out how to get data from two urls for same plot
Plotly.d3.json("/samples/BB_940", function(error, response) {
  if (error) return console.warn(error);
  top_otu = response[0].otu_id.slice(0,9);
  top_values = response[0].value.slice(0,9);
  console.log(top_otu);
  console.log(top_values);
  data = [{
    "labels": top_otu,
    "values": top_values,
    "type": "pie"
  }];
  var PIE = document.getElementById('pie');
  Plotly.newPlot(PIE, data);
})

// handle change in option dropdown
function optionChanged(option) {
  // TODO: complete function
  console.log(option);

}
