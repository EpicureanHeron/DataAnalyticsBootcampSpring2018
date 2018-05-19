// create map
var myMap = L.map("map", {
  center: [37.09, -95.71],
  zoom: 5
});

// Adding tile layer
L.tileLayer("https://api.mapbox.com/styles/v1/mapbox/outdoors-v10/tiles/256/{z}/{x}/{y}?" +
  "access_token=pk.eyJ1IjoiZGRyb3NzaTkzIiwiYSI6ImNqZ3d2NHVmdjFnN2cyd216dnFzcGk1ancifQ.wgmwHuLPLzum1yLj5Ffwqw").addTo(myMap);

// JSON link
var link = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_week.geojson";


d3.json(link, function(data) {
  var features = data["features"];
  // L.geoJson(data["features"]).addTo(map);

  for (var i = 0; i < features.length; i++) {
    var geometry = features[i]["geometry"]["coordinates"];
    var magnitude = features[i]["properties"]["mag"];
    var coords = {
      longitude: geometry["0"],
      latitude: geometry["1"]
    };
    //   var city = cities[i];
    var latlng = L.latLng(coords.latitude, coords.longitude);
    var circle = L.circle(latlng, {
      color: getColor(magnitude),
      fillOpacity: 0.75,
      radius: magnitude * 10000
    }).addTo(myMap);
    //
    //
    //   L.circle(city.locatsion)
    //     .bindPopup("<h1>" + city.name + "</h1> <hr> <h3>Population " + city.population + "</h3>")
    //     .addTo(myMap);
    // }

  }

});

function getColor(mag) {
  var color = '';
  if (mag < 1.5){
    color = 'green';
  }
  else if (mag > 1.5 && mag < 3) {
    color = 'yellow';
  }
  else if (mag > 3) {
    color = 'red'
  }
  console.log(color);
  return color;
}
