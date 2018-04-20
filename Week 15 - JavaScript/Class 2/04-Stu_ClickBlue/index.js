// Getting references to the h1 tag that will display the count, the increment, and decrement buttons
var $count = document.querySelector(".panel h1");
var $incrementBtn = document.querySelector(".panel .btn.btn-primary");
var $decrementBtn = document.querySelector(".panel .btn.btn-danger");


// var fn1 = function(event) {
//   console.log(event);
// }

// // A callback function is called in response to a click of the increment button
// $incrementBtn.addEventListener("click", fn1);
// // Likewise with the decrement button
// $decrementBtn.addEventListener("click", function(event) {
//   console.log(event);
// });


// Add click event listeners to the buttons, call the functions passed in
$incrementBtn.addEventListener("click", handleIncrementClick);
$decrementBtn.addEventListener("click", handleDecrementClick);

// Initialize the count at 0
var count = 0;
var size = 36;
var red = 0;
var blue = 0;
// Render the count value to the page for the first time when it loads
renderCount();

function renderCount() {
  // Update the inner text of the $count element
  $count.innerText = count;
  console.log("Rendering: " + count)
}

// handleDecrementClick decreases count by 1 and re-renders the count to DOM
function handleDecrementClick() {
  count--;
  size -= 2;
  blue -= 30;
  red += 50;
  $count.style.fontSize = size.toString() + "px";
  $count.style.color = "rgb(" + red.toString() + ", 0, 0)";
  renderCount();
}

// handleIncrementClick increases count by 1 and re-renders the count to DOM
function handleIncrementClick() {
  count += 2;
  size += 2;
  red -= 30;
  blue += 50;
  $count.style.fontSize = size.toString() + "px";
  $count.style.color = "rgb(0, 0, " + blue.toString() + ")";
  renderCount();
}
