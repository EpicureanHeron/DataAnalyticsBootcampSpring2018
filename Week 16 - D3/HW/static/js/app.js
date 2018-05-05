// populate option dropdown
Plotly.d3.json("/names", function(error, response) {
  var $select = document.getElementById('selDataset')

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
  if (error)
    return console.warn(error);
  top_otu = response[0].otu_id.slice(0, 9);
  top_values = response[0].value.slice(0, 9);
  data = [
    {
      "labels": top_otu,
      "values": top_values,
      "type": "pie"
    }
  ];
  var PIE = document.getElementById('pie');
  Plotly.newPlot(PIE, data);
})

// create default bubble chart
// TODO: figure out how to get data from two urls for same plot
Plotly.d3.json("/samples/BB_940", function(error, response) {
  if (error)
    return console.warn(error);
  var trace1 = {
    x: response[0].otu_id,
    y: response[0].value,
    mode: 'markers',
    marker: {
      color: response[0].otu_id,
      size: response[0].value
    }
  };
  data = [trace1];
  var BUBBLE = document.getElementById('bubble');
  Plotly.newPlot(BUBBLE, data);
})

// display default metadata
Plotly.d3.json("/metadata/BB_940", function(error, response) {
  console.log(response);
  console.log(Object.keys(response));
  // totally a much better way to do this that I don't know about
  var $tbody = document.querySelector("tbody");
  for (var i = 0; i < response.length; i++) {
    var entry = response[i];
    var fields = Object.keys(entry);
    var $row = $tbody.insertRow(i);
    for (var j = 0; j < fields.length; j++) {
      var field = fields[j];
      var $cell = $row.insertCell(j);
      $cell.innerText = entry[field];
      $cell.id = field;
    }
  }

});

function updatePie(newData) {
  var PIE = document.getElementById('pie');
  Plotly.restyle(PIE, 'labels', [newData[0].otu_id.slice(0, 9)]);
  Plotly.restyle(PIE, 'values', [newData[0].value.slice(0, 9)]);
}

function updateBubble(newData) {
  var BUBBLE = document.getElementById('bubble');
  Plotly.restyle(BUBBLE, 'x', [newData[0].otu_id]);
  Plotly.restyle(BUBBLE, 'y', [newData[0].value]);
  // im not sure if this is actually updating the size...
  Plotly.restyle(BUBBLE, 'marker{size}', [newData[0].value]);

}

function updateMeta(path) {
  var $AGE = document.getElementById("AGE");
  var $BBTYPE = document.getElementById("BBTYPE");
  var $ETHNICITY = document.getElementById("ETHNICITY");
  var $GENDER = document.getElementById("GENDER");
  var $LOCATION = document.getElementById("LOCATION");
  var $SAMPLEID = document.getElementById("SAMPLEID");

  Plotly.d3.json(`/metadata/${path}`, function(error, data) {
    console.log("meta", data);
    $AGE.innerHTML = data[0].AGE
    $BBTYPE.innerHTML = data[0].BBTYPE
    $ETHNICITY.innerHTML = data[0].ETHNICITY
    $GENDER.innerHTML = data[0].GENDER
    $LOCATION.innerHTML = data[0].LOCATION
    $SAMPLEID.innerHTML = data[0].SAMPLEID
  });
}

// handle change in option dropdown
function optionChanged(option) {
  console.log(option);
  Plotly.d3.json(`/samples/${option}`, function(error, data) {
    console.log("newdata", data);
    updatePie(data);
    updateBubble(data);
    updateMeta(option);
  });
}
