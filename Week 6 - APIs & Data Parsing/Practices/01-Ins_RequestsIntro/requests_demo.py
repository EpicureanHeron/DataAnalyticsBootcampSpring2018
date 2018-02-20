# Dependencies
import requests as req
import json

# URL for GET requests to retrieve vehicle data
url = "https://api.spacexdata.com/v2/launchpads"

# Print the response object to the console
# print(req.get(url))

# Retrieving data and converting it into JSON
# print(req.get(url).json())

# Pretty Print the output of the JSON
response = req.get(url).json()
print(json.dumps(response, indent=4, sort_keys=True))
