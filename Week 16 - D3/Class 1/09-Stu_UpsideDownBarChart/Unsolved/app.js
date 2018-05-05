// Dataset we will be using to set the height of our rectangles
var booksReadThisYear = [17, 23, 20, 34];

// Append an SVG wrapper to the page and set a variable equal to a reference to it
// YOUR CODE HERE
var $svg = d3.select('#svg-area').append('svg');

$svg.attr('width', '1500px').attr('height', '1500px');

// Vertical Bar Chart
// YOUR CODE HERE
$bar = $svg.selectAll('rect');

$bar.data(booksReadThisYear)
    .enter()
    .append('rect')
    .attr('x', function(d,i) {
        return i * 55;
    })
    .attr('y', 20)
    .attr('width', 50)
    .attr('height', function(d) {
        return d * 3;
    })
    .style('fill', '#13c0d7');


// BONUS
// Horizontal Bar Chart
// YOUR CODE HERE
$bar.data(booksReadThisYear)
    .enter()
    .append('rect')
    .attr('x', 10)
    .attr('y',function(d,i) {
        return (i * 55)+100;
    })
    .attr('width', function(d) {
        return d * 3;
    })
    .attr('height', 50)
    .style('fill', '#13c0d7');
// BONUS 2
// Alter your Vertical bar chart code to go from bottom  up.
$bar.data(booksReadThisYear)
    .enter()
    .append('rect')
    .attr('x', function(d,i) {
        return i * 75;
    })
    .attr('y', 500)
    .attr('width', 50)
    .attr('height', function(d) {
        return d;
    })
    .attr('transform', 'rotate(90 140 105)')
    .style('fill', '#13c0d7');
