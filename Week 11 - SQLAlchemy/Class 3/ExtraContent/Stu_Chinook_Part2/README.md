# Chinook Database Analysis Part 2

* In part 2 of this activity, you will create Flask api routes to return data from the queries that you designed in part 1 of the assignment.

## Instructions

* Create a file called `app.py` for your Flask app.

* Use SQLAlchemy to import the database `chinook.sqlite` and reflect all of the tables into ORM classes. For this activity, we will only need the `invoices` table and the `invoice_items` table.

* Initialize your flask app and save it to a variable called `app`.

* Uncomment the `/` route provided and use it as a guide to complete the missing routes. For each of the routes listed, you will need to create a route that returns the database query results from part 1 of the activity in JSON format.

* Define a **GET** route called `/api/v1.0/countries` that returns a list of Billing Countries.

* Define a **GET** route called `/api/v1.0/countries/invoice/totals` that returns a list of Invoice Totals by Billing Country.

  * Return a list of dictionaries with `country` and `total` as the keys. Use the query results as the values.

* Define a **GET** route called `/api/v1.0/postalcodes/<country>` that returns a list of Billing postal codes for a given country. Use 'USA' as the default country if no country is supplied.

* Define a **GET** route called `/api/v1.0/invoice/total/<country>` that returns the invoice items total for a specific country. Use 'USA' as the default country if not country is supplied.

* Define a **GET** route called `/api/v1.0/postalcodes/totals/<country>` that returns the invoice totals per billing postal code for a specific country. Use 'USA' as the default country if not country is supplied.

  * Return a list of dictionaries with `postal_code` and `invoice_total` as the keys. Use the query results as values.

## HINTS

* Use Flask Jsonify to return your results as json data.

* Convert the data to JSON friendly values when necessary (i.e. convert sqlite Decimal type to Python Float before using jsonify).

- - -

### Copyright

Trilogy Education Services © 2017. All Rights Reserved.
