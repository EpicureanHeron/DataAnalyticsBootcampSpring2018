var mymap = L.map('mapid').setView([
  37.09, -95.71
], 5);

L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}', {
  attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
  maxZoom: 18,
  id: 'mapbox.streets',
  accessToken: 'pk.eyJ1IjoiZGRyb3NzaTkzIiwiYSI6ImNqZ3d2NHVmdjFnN2cyd216dnFzcGk1ancifQ.wgmwHuLPLzum1yLj5Ffwqw'
}).addTo(mymap);

// City markers

// Add code to create a marker for each city below and add it to the map

// newyork;
var marker = L.marker([40.712775, -74.005973]).addTo(mymap);

// chicago;
var marker = L.marker([41.878114, -87.629798]).addTo(mymap);

// houston;
var marker = L.marker([29.760427, -95.369803]).addTo(mymap);

// la;
var marker = L.marker([34.052234, -118.243685]).addTo(mymap);

// omaha;
var marker = L.marker([41.256537, -95.934503]).addTo(mymap);
