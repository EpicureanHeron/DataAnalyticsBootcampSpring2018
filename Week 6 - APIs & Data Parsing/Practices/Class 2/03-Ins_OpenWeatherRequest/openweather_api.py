# Dependencies
import json
import requests as req

# Save config information
api_key = "25bc90a1196e6f153eece0bc0b0fc9eb"
url = "http://api.openweathermap.org/data/2.5/weather?"
city = "London"

# Build query URL
query_url = url + "appid=" + api_key + "&q=" + city

# Get weather data
weather_response = req.get(query_url)
weather_json = weather_response.json()

# Get the temperature from the response
print("The weather API responded with: " + str(weather_json) + ".")
