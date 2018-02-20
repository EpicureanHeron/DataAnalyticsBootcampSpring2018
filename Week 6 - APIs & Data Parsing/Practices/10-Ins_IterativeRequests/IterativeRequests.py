# Dependencies
import random
import json
import requests

# Let's get the JSON for 100 posts sequentially.
url = "http://jsonplaceholder.typicode.com/posts/"
response_json = []

# Create random indices representing, for instance, a user's choice of posts
indices = random.sample(list(range(1, 100)), 10)

for i in range(0, len(indices)):
    print("Making request number " + str(i) +
          " for ID " + str(indices[i]) + ".")

    # Get post #i
    post_response = requests.get(url + str(indices[i]))

    # Save post's JSON
    response_json.append(post_response.json())

# Now we have 10 post objects, which we got by making 100 requests to the API.
print("We have " + str(len(response_json)) + " posts!")
