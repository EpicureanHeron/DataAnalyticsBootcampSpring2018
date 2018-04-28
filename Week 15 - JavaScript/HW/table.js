var $tbody = document.querySelector("tbody");
var $dateTimeInput = document.querySelector("#datetime_search");
var $cityInput = document.querySelector("#city_search");
var $stateInput = document.querySelector("#state_search");
var $countryInput = document.querySelector("#country_search");
var $shapeInput = document.querySelector("#shape_search");
var $searchBtn = document.querySelector("#search");
var $resetBtn = document.querySelector("#reset");

$searchBtn.addEventListener("click", handleSearchButtonClick);
$resetBtn.addEventListener("click", resetTable);

var UFOData = dataSet;

function renderTable() {
  $tbody.innerHTML = "";
  for (var i = 0; i < UFOData.length; i++) {
    var entry = UFOData[i];
    var fields = Object.keys(entry);
    var $row = $tbody.insertRow(i);
    for (var j = 0; j < fields.length; j++) {
      var field = fields[j];
      var $cell = $row.insertCell(j);
      $cell.innerText = entry[field];
    }
  }
}

function handleSearchButtonClick() {
  var filterDateTime = $dateTimeInput.value.trim().toLowerCase();
  var filterCity = $cityInput.value.trim().toLowerCase();
  var filterState = $stateInput.value.trim().toLowerCase();
  var filterCountry = $countryInput.value.trim().toLowerCase();
  var filterShape = $shapeInput.value.trim().toLowerCase();

  if (filterDateTime) {
    UFOData = UFOData.filter(function(entry) {
      var entryDateTime = entry.datetime.toLowerCase();

      return entryDateTime === filterDateTime;
    });
  }

  if (filterCity) {
    UFOData = UFOData.filter(function(entry) {
      var entryCity = entry.city.toLowerCase();

      return entryCity === filterCity;
    });
  }

  if (filterState) {
    UFOData = UFOData.filter(function(entry) {
      var entryState = entry.state.toLowerCase();

      return entryState === filterState;
    });
  }

  if (filterCountry) {
    UFOData = UFOData.filter(function(entry) {
      var entryCountry = entry.country.toLowerCase();

      return entryCountry === filterCountry;
    });
  }

  if (filterShape) {
    UFOData = UFOData.filter(function(entry) {
      var entryShape = entry.shape.toLowerCase();

      return entryShape === filterShape;
    });
  }

  renderTable();
}

function resetTable() {
  UFOData = dataSet;
  $dateTimeInput.value = "";
  $cityInput.value = "";
  $stateInput.value = "";
  $countryInput.value = "";
  $shapeInput.value = "";
  renderTable();
  // TODO: set input values to ""
}

renderTable();
