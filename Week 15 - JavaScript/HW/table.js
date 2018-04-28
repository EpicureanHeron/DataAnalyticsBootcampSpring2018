// Get references to the tbody element, input field and button
var $tbody = document.querySelector("tbody");
var $dateTimeInput = document.querySelector("#datetime_search");
var $searchBtn = document.querySelector("#search");
var $resetBtn = document.querySelector("#reset");

// Add an event listener to the searchButton, call handleSearchButtonClick when clicked
$searchBtn.addEventListener("click", handleSearchButtonClick);
$resetBtn.addEventListener("click", resetTable);

// Set filteredentryes to entryData initially
function resetTable() {

}
var UFOData = dataSet;

// renderTable renders the filteredentryes to the tbody
function renderTable() {
  $tbody.innerHTML = "";
  for (var i = 0; i < UFOData.length; i++) {
    // Get get the current entry object and its fields
    var entry = UFOData[i];
    var fields = Object.keys(entry);
    // Create a new row in the tbody, set the index to be i + startingIndex
    var $row = $tbody.insertRow(i);
    for (var j = 0; j < fields.length; j++) {
      // For every field in the entry object, create a new cell at set its inner text to be the current value at the current entry's field
      var field = fields[j];
      var $cell = $row.insertCell(j);
      $cell.innerText = entry[field];
    }
  }
}

function handleSearchButtonClick() {
  // Format the user's search by removing leading and trailing whitespace, lowercase the string
  console.log("in search handlers");
  console.log($dateTimeInput.value.trim().toLowerCase());
  var filterDateTime = $dateTimeInput.value.trim().toLowerCase();

  // Set filteredentryes to an array of all entryes whose "state" matches the filter
  UFOData = UFOData.filter(function(entry) {
    var entryDateTime = entry.datetime.toLowerCase();

    // If true, add the entry to the filteredentryes, otherwise don't add it to filteredentryes
    return entryDateTime === filterDateTime;
  });

  renderTable();
}

function resetTable() {
  UFOData = dataSet;
  renderTable();
}

// Render the table for the first time on page load
renderTable();
