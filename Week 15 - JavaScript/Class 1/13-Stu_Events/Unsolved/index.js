// Set variable for the button
var clickButton = document.querySelector("#clickHere");

// Add click even listener to the button
clickButton.addEventListener("click", function() {
  // pop is an Array method which removes the last element

  // Prompt user for favorite color
  userColor = prompt("What is your favorite color?: ");
  // Create paragraph element
  paragraph = document.querySelector("#color");

  // Add new html line to color
  paragraph.innerHTML = "Favoite Color: " + userColor;
});
