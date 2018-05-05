// Answer the following questions after discussing with a partner.

/* 1. What does SVG stand for?  How are they used with D3? */
Scalable Vector Graphics
/* 2.  What is data binding? */
data binding is connecting an array of data in JS to a part of the webpage
/* 3.  Given the following and a an HTML page with no elements currently in the body,
use the enter pattern to render three <li> elements to the page with text matching
the integers in the array. */

var arr = [1, 2, 3]
var ul = d3.select("body").append("ul")
//YOUR CODE HERE//
d3.select('ul')
  .selectAll('li')
  .data(arr)
  .enter()
  .append('li')
  .text(function (d) {
    return d;
  })


/* 4. Imagine three <li> elements already exists on the page.  Create code to update the text of that element while also adding three new elements
to match the array below. */
var arr = [1, 1, 2, 3, 5, 8]
var ul = d3.select("ul")
// YOUR CODE HERE //
var selection = d3.select('ul')
  .selectAll('li')
  .data(arr)
  .enter()
  .append("li")
  .merge(selection)
  .text(function (d) {
    return d;
  })

/* Bonus - Make the code in number 4 more concise by using the ES6 syntax for arrow functions.  Then, modify the code to set the text of each
element to "(index in the array): (item from the array) */
// YOUR CODE HERE //
