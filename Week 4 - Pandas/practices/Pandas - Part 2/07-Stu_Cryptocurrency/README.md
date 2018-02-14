**Instructions**

* Read in `bitcoin_cash_price.csv` and `dash_price.csv` and print out their DataFrames

* Perform an inner merge that combines both DataFrames on the "Date" column

* Rename the columns within the newly merged DataFrame so that the headers are more descriptive (e.g. "Bitcoin Open", "Bitcoin Close", ...)

* Create a summary table that includes the following information: `Best Bitcoin Open`, `Best Dash Open`, `Best Bitcoin Close`, `Best Dash Close`, `Total Bitcoin Volume`, `Total Dash Volume`

* `Total Bitcoin Volume` and `Total Dash Volume` should be calculated to have units of "millions" and be rounded to two decimal places (use the built-in `round()` function)