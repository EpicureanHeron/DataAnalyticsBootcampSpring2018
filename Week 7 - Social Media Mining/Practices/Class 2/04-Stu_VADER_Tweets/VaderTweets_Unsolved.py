# Dependencies
import tweepy
import json
import numpy as np

# Twitter API Keys. Place your keys here.
consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""

# Setup Tweepy API Authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Target User Account
target_user = "@DalaiLama"

# Lists for holding sentiments
compound_list = []
positive_list = []
negative_list = []
neutral_list = []

# 
for page in tweepy.Cursor(api.user_timeline, id=target_user).pages(200):
    # page is a list of statuses

    # Loop through all tweets
    for tweet in page:
        tweet_text = json.dumps(tweet._json, indent=3)
        tweet = json.loads(tweet_text)

        # Parse the tweet to identify its text

        # Analyze the sentiment of the tweet

        # Add the sentiment analyses to the respective lists

# Print the average sentiments of the tweets
