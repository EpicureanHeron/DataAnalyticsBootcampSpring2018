/* data route */
var url = "/names";



Plotly.d3.json(url, function(error, response) {
  console.log(response);
  $select = document.getElementById('selDataset')

  for (var i = 0; i < response.length; i++) {
    var option = document.createElement("option");
    option.value = response[i];
    option.innerHTML = response[i]

    $select.appendChild(option);
  }

});
