// Getting references to the input fields, button, and lists
var $nameInput = document.querySelector("#name");
var $itemInput = document.querySelector("#item");
var $perishableInput = document.querySelector("#perishable");

var $submitBtn = document.querySelector("#submit");
var $priority = document.querySelector("#priority");
var $nonPriority = document.querySelector("#non-priority");

// When the submit button is clicked, call the handleSubmitClick function
$submitBtn.addEventListener("click", handleSubmitClick);

// When an element with the id of "RemovalButton" is clicked, call the removePatron function
$priority.addEventListener("click", removeOrder);
$nonPriority.addEventListener("click", removeOrder);

// Trigger event handler when the Submit button is clicked
function handleSubmitClick(event) {
  // The default behavior of a button clicked inside of a form is to try and submit the form somewhere (which we don't want)
  event.preventDefault();

  // Create a new movie patron object that will hold the data used to populate the page
  var newOrder = {
    name: $nameInput.value.trim(),
    item: $itemInput.value.trim(),
    perishable: $perishableInput.value.trim()
  };

  // Clear the input fields
  $nameInput.value = "";
  $itemInput.value = "";
  $perishableInput.value = "";

  // Since we will always be creating a list item and removal button, declare these elements outside of the if statement so we do not repeat code
  var $listButton = document.createElement("button");
  $listButton.className = "list-group-item list-group-item-action";
  $listButton.class = "RemovalButton";
  $listButton.innerText = newOrder.name + ", " + newOrder.item;
  // console.log(newOrder.name);

  // TODO: Classify order as Priority if it is perishable
  if (newOrder.perishable.toLowerCase() === "yes" || newOrder.perishable.toLowerCase() === "y") {
    $priority.appendChild($listButton);
  }
  else {
    $nonPriority.appendChild($listButton);
  }
}
// Function to remove an item from the orders
function removeOrder(event) {
  // The element that is clicked
  var $elementClicked = event.target;
  // Assign a variable to the element's parent element
  var parent = $elementClicked.parentElement;
  // Remove the clicked element from the parent
  parent.removeChild($elementClicked);
  // Prevent the page from refreshing
  return false;
}
