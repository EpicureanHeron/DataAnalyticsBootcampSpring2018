var mymap = L.map('mapid').setView([
  45.52, -122.67
], 13);

L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}', {
  attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
  maxZoom: 18,
  id: 'mapbox.streets',
  accessToken: 'pk.eyJ1IjoiZGRyb3NzaTkzIiwiYSI6ImNqZ3d2NHVmdjFnN2cyd216dnFzcGk1ancifQ.wgmwHuLPLzum1yLj5Ffwqw'
}).addTo(mymap);


var circle = L.circle([45.511, -122.595], {
    color: 'red',
    fillColor: '#f03',
    fillOpacity: 0.5,
    radius: 700
}).addTo(mymap);

var polygon = L.polygon([
    [45.50, -122.67],
    [45.51, -122.675],
    [45.50, -122.68]
]).addTo(mymap);

// create a red polyline from an array of LatLng points
var latlngs = [
  [45.545, -122.6747],
  [45.5345, -122.687]
];
var polyline = L.polyline(latlngs, {color: 'red'}).addTo(mymap);
