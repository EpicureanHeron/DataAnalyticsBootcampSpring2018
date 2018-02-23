# Dependencies
import json
import requests

# Let's get the JSON for 100 posts sequentially.
url = "http://www.omdbapi.com/?t="
api_key = "&apikey=40e9cece"
responses = []

movies = ["Aliens", "Sing", "Moana"]

for movie in movies:
    response = requests.get(url + movie + api_key).json()
    responses.append(response)
    print('The Director for ' + movie + ' is ' + response['Director'])

print(responses)