# Dependencies
import requests as req

# Performing a GET Request and saving the API's response within a variable
url = "https://api.spacexdata.com/v2/rockets/falcon9"
response = req.get(url)
response_json = response.json()

# It is possible to grab a specific value from within the JSON object
print(response_json["cost_per_launch"])

# It is also possible to perform some analyses on values stored within the JSON object
print("There are " + str((len(response_json["payload_weights"]))) + " payloads.")

# Finally, it is possible to reference the values stored within sub-dictionaries and sub-lists
print("The first payload weighed " + str(response_json["payload_weights"][0]["kg"]) + " Kilograms")
