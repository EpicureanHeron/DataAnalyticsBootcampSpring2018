# Dependencies
import json
import requests

# Google developer API key
gkey = "AIzaSyA_Clyz3478YAUnsESNHE5dyktvvMoa-vw"

# Target city
# Boise, Idaho {"lat": 43.6187102, "lng": -116.2146068}
# New York, NY {"lat": 40.7128, "lng": -74.0059}
target_city = {"lat": 43.6187102, "lng": -116.2146068}

# Build the endpoint URL (Checks all ice cream shops)
target_url = "https://maps.googleapis.com/maps/api/place/radarsearch/json" \
    "?location=%s,%s&radius=8000&keyword=ice+cream&type=food&key=%s" % (
        target_city["lat"], target_city["lng"], gkey)

# Print the assembled URL (visit this URL)
print(target_url)

# Run a request to endpoint and convert result to json
ice_cream_data = requests.get(target_url).json()

# Print the number of ice cream shops
print(len(ice_cream_data["results"]))
