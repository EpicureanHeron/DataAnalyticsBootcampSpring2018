# Dependencies
import requests as req
import json

# URL for GET requests to retrieve company info about SpaceX
url = "https://api.spacexdata.com/v2/info"

# get response in JSON format
response = req.get(url).json()

# print specific record
# print(response['founder'])

# print all
print(json.dumps(response, indent=4, sort_keys=True))
