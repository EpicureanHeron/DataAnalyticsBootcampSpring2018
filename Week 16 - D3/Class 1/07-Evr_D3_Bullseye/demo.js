var $svg = d3.select("body").append("svg");

$svg.attr("width", "100px").attr("height", "100px");

$circles = $svg.selectAll("circle");

var r_values = [40, 25, 10];

$circles.data(r_values)
    .enter()
    .append("circle")
    .attr("cx", 50)
    .attr("cy", 50)
    .attr("r", function(d) {
        return d;
    })
    .attr("stroke", "black")
    .attr("stroke-width", "5")
    .attr("fill", "red");
