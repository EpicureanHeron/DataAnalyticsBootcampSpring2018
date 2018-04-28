function init() {
  var data = [
    {
      values: [
        19, 26, 55, 88
      ],
      labels: [
        "Spotify", "Soundcloud", "Pandora", "Itunes"
      ],
      type: "pie"
    }
  ];

  var layout = {
    height: 600,
    width: 800
  };

  Plotly.plot("pie", data, layout);
}

function updatePlotly(newdata) {
  // YOUR CODE HERE
  var pie = document.getElementById("pie");
  Plotly.restyle(pie, "values", [newdata]);
  // Use `Plotly.restyle` to update the pie chart with the newdata array
}

function getData(dataset) {
  // YOUR CODE HERE
  switch (dataset) {
    case "dataset1":
      var data = [5, 28, 18, 50];
      break;
    case "dataset2":
      var data = [5, 82, 17, 31];
      break;
    case "dataset3":
      var data = [3, 92, 63, 88];
      break;
  }
  // create a select statement to select different data arrays (YOUR CHOICE)
  // whenever the dataset parameter changes. This function will get called
  // from the dropdown event handler.
  updatePlotly(data);
}

init();
