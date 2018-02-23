# Google Complex (Airport)

In this activity we are tasked with creating a Data Frame containing the rating of every airport in the top 100 metropolitan areas according to Google Users.

## Instructions

* Using [Airport_Ratings_Unsolved.ipynb](Unsolved/Airport_Ratings_Unsolved.ipynb) as a starting point, utilize the Google Geocoding API, the Google Places API, and Python/Jupyter, create a script that lists the "Airport Rating" of the major "International Airport" in each the top 100 metropolitan areas found in [Cities.csv](Unsolved/Cities.csv).

* Your final `ipynb` file should contain each of the following headers: 

  1. `City`

  2. `State`

  3. `Lat`

  4. `Lng`

  5. `Airport Name`

  6. `Airport Address`

  7. `Airport Rating`

### Hints

* You will need to obtain the lat/lng of each airport prior to sending it through the Google Places API to obtain the rating.

* When using the Google Places API, be sure to use the term: "International Airport" to ensure that the airport you receive data for is the major airport in the city and not a regional one.

* Use a try-except to skip airports for which there are no Google user ratings.
