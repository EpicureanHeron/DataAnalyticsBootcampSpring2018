# Dependencies
import tweepy
import json
import config

# Twitter API Keys
# Twitter API Keys
consumer_key = config.consumer_key
consumer_secret = config.consumer_secret
access_token = config.access_token
access_token_secret = config.access_token_secret

# auth tweepy
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())

# Note: Twitter prevents tweeting the same status or message multiple
# times. Be sure to change the text when testing.

# Create two status updates
#api.update_status('Me Tweet')

# Create a status update with an image

# Create a friendship with another user

# Send a direct message to another user (Hint: You will need them to
# follow your account)

# Bonus: Retweet any tweet from someone else's account (Hint: You will
# need to locate a tweet's id)

get_id = api.home_timeline(count=1)

delete_id = get_id[0]['id']
# Bonus: Delete your most recent tweet (Hint: "Destroy")
api.destroy_status(delete_id)

# Bonus: Delete your most recent sent message (Hint: "Destroy")
