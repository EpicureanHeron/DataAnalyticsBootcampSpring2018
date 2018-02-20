# Dependencies
import requests as req
import json

# URL for GET requests to retrieve Star Wars character data
url = "https://swapi.co/api/people/"

# Storing the JSON response within a variable
response = req.get(url + '4').json()

# Collecting the name of the character collected

# Counting how many films the character was in

# Figure out what their first starship was
# get starship API URL
starship_url = response['starships'][0]
# get starship API data in JSON
starship = req.get(starship_url).json()

# Print character name and how many films they were in
print(response['name'] + ' was in ' + str(len(response['films'])) + " films")

# Print what their first ship was
print('His first starship was the ' + starship['name'])
