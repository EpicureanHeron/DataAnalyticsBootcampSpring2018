
var svgWidth = 960;
var svgHeight = 720;

var margin = {
  top: 20,
  right: 40,
  bottom: 60,
  left: 100
};

var width = svgWidth - margin.left - margin.right;
var height = svgHeight - margin.top - margin.bottom;

var svg = d3.select("#plot")
  .append("svg")
  .attr("width", svgWidth)
  .attr("height", svgHeight)

var chartGroup = svg.append("g")
  .attr("transform", `translate(${margin.left}, ${margin.top})`);

d3.csv("data.csv", function (err, incomeData) {
  if (err) throw err;


  incomeData.forEach(function (data) {
    data.medianIncome = +data.medianIncome;
    data.noDoctor = data.noDoctor;
  });

  var xLinearScale = d3.scaleLinear()
    .domain([35000, d3.max(incomeData, d => d.medianIncome)])
    .range([0, width]);

  var yLinearScale = d3.scaleLinear()
    .domain([5, 20])
    .range([height, 10]);

  var bottomAxis = d3.axisBottom(xLinearScale);
  var leftAxis = d3.axisLeft(yLinearScale);

  chartGroup.append("g")
    .attr("transform", `translate(0, ${height})`)
    .call(bottomAxis);

  chartGroup.append("g")
    .call(leftAxis);

  var circlesGroup = chartGroup.selectAll("circle")
  .data(incomeData)
  .enter()
  .append("g")

  circlesGroup.append("circle")
  .attr("cx", d => xLinearScale(d.medianIncome))
  .attr("cy", d => yLinearScale(d.noDoctor))
  .attr("r", "15")
  .attr("fill", "blue")
  .attr("opacity", ".5")

  circlesGroup.append("text")
  .text(function (d) {
    console.log(d.stateAbbr);
    return d.stateAbbr;
  })
  .attr("x",function (d) {
    return xLinearScale(d.medianIncome - 550);
  })
  .attr("y", function (d) {
    return yLinearScale(d.noDoctor - 0.1);
  })

  var toolTip = d3.tip()
    .attr("class", "tooltip")
    .offset([80, -60])
    .html(d =>
      `${d.state}<br>Hair Median Income: ${d.medianIncome}<br>No Doctor %: ${d.noDoctor}%`
    );

  chartGroup.call(toolTip);

  circlesGroup.on("mouseover", function (incomeData) {
      toolTip.show(incomeData);
    })
    .on("mouseout", function (incomeData, index) {
      toolTip.hide(incomeData);
    });

  chartGroup.append("text")
    .attr("transform", "rotate(-90)")
    .attr("y", 0 - margin.left + 40)
    .attr("x", 0 - (height * 0.6))
    .attr("dy", "1em")
    .attr("class", "axisText")
    .text("% That Don't Go To Doctor Because of $");

  chartGroup.append("text")
    .attr("transform", `translate(${width * 0.4}, ${height + margin.top + 30})`)
    .attr("class", "axisText")
    .text("Median Income ($)");
});
