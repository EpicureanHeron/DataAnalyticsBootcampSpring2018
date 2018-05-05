/**
 * Helper function to select stock data
 * Returns an array of values
 * @param {array} rows
 * @param {integer} index
 * index 0 - Date
 * index 1 - Open
 * index 2 - High
 * index 3 - Low
 * index 4 - Close
 * index 5 - Volume
 */
function unpack(rows, index) {
  return rows.map(function(row) {
    return row[index];
  });
}

// Calculate a rolling average for an array
function rollingAverage(arr, windowPeriod = 10) {
  // @TODO: YOUR CODE HERE
  var rolling_averages = [];
  var sum = 0;
  var count = 0;
  var window_nums = [];
  for (var i = 0; i < arr.length; i++) {
    window_nums.push(arr[i]);

    if (window_nums.length >= 30) {
      for (var j = 0; j < window_nums.length; j++) {
        sum += window_nums[j];
      }
      window_nums.shift();
      rolling_avg = sum / windowPeriod;
      sum = 0;
      rolling_averages.push(rolling_avg);
    }
  }
  console.log(rolling_averages);
  return rolling_averages;
}

// Submit Button handler
function handleSubmit() {
  // Prevent the page from refreshing
  Plotly.d3.event.preventDefault();

  // Select the input value from the form
  var stock = Plotly.d3.select("#stockInput").node().value;
  console.log(stock);

  // clear the input value
  Plotly.d3.select("#stockInput").node().value = "";

  // Build the plot with the new stock
  buildPlot(stock);
}

function buildPlot(stock) {
  var apiKey = "YOUR_API_KEY";

  var url = `https://www.quandl.com/api/v3/datasets/WIKI/${stock}.json?start_date=2016-10-01&end_date=2017-10-01&api_key=${apiKey}`;

  Plotly.d3.json(url, function(error, response) {

    if (error)
      return console.warn(error);

    // Grab values from the response json object to build the plots
    var name = response.dataset.name;
    var stock = response.dataset.dataset_code;
    var startDate = response.dataset.start_date;
    var endDate = response.dataset.end_date;
    var dates = unpack(response.dataset.data, 0);
    var openingPrices = unpack(response.dataset.data, 1);
    var highPrices = unpack(response.dataset.data, 2);
    var lowPrices = unpack(response.dataset.data, 3);
    var closingPrices = unpack(response.dataset.data, 4);

    // Calculate Rolling averages with a window of 30 days
    var rollingPeriod = 30;
    var rollingAvgClosing = rollingAverage(closingPrices, rollingPeriod);

    var trace1 = {
      type: "scatter",
      mode: "lines",
      name: name,
      x: dates,
      y: closingPrices,
      line: {
        color: "#17BECF"
      }
    };

    // Candlestick Trace
    var trace2 = {
      type: "candlestick",
      x: dates,
      high: highPrices,
      low: lowPrices,
      open: openingPrices,
      close: closingPrices
    };

    // Rolling Averages Trace
    var trace3 = {
      // YOUR CODE HERE
      type: "scatter",
      mode: "lines",
      name: "Rolling Average",
      x: dates,
      y: rollingAvgClosing
    };

    var data = [trace1, trace2, trace3];

    var layout = {
      title: `${stock} closing prices`,
      xaxis: {
        range: [
          startDate, endDate
        ],
        type: "date"
      },
      yaxis: {
        autorange: true,
        type: "linear"
      }
    };

    Plotly.newPlot("plot", data, layout);

  });
}

// Add event listener for submit button
Plotly.d3.select("#submit").on("click", handleSubmit);
