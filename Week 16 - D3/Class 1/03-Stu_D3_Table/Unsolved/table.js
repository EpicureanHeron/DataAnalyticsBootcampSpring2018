var austin_weather = [{
    date: "2018-02-01",
    low: 51,
    high: 76
  },
  {
    date: "2018-02-02",
    low: 47,
    high: 59
  },
  {
    date: "2018-02-03",
    low: 44,
    high: 59
  },
  {
    date: "2018-02-04",
    low: 52,
    high: 73
  },
  {
    date: "2018-02-05",
    low: 47,
    high: 71
  },
]
// YOUR CODE HERE
d3.select("tbody")
  .selectAll("tr")
  .data(austin_weather)
  .enter() // creates placeholder for new data
  .insert("tr") // appends a div to placeholder
  .html(function (d) {
    return `<td>${d.date}</><td>${d.low}</><td>${d.high}</>`
  }); // sets the html in the div to an image tag with the link
