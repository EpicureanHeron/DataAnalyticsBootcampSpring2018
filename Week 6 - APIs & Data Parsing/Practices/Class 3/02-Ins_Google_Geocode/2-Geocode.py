# Dependencies
import requests

# Google developer API key
gkey = "AIzaSyA_Clyz3478YAUnsESNHE5dyktvvMoa-vw"

# Target city
target_city = "Boise, Idaho"

# Build the endpoint URL
target_url = "https://maps.googleapis.com/maps/api/geocode/json" \
    "?address=%s&key=%s" % (target_city, gkey)

# Print the assembled URL
print(target_url)

# Run a request to endpoint and convert result to json
geo_data = requests.get(target_url).json()

# Print the json
print(geo_data)
