# Dependencies
import tweepy
import json
import numpy as np
import config
# Import and Initialize Sentiment Analyzer
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
analyzer = SentimentIntensityAnalyzer()

# TODO: move keys to config file and import from there
# twitter keys
# Twitter API Keys
consumer_key = config.consumer_key
consumer_secret = config.consumer_secret
access_token = config.access_token
access_token_secret = config.access_token_secret

# auth tweepy
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Target Search Term
target_terms = ("@SouthwestAir", "@AmericanAir", "@SpiritAirlines",
                "@Virginatlantic", "@Delta", "@AlaskaAir", "@KLM")

# "Real Person" Filters
min_tweets = 5
max_tweets = 10000
max_followers = 2500
max_following = 2500
lang = "en"

# Array to hold sentiment
sentiment_array = []

# Variable for holding the oldest tweet
oldest_tweet = ""

def is_human(tweet):
    return tweet['user']['followers_count'] > 200 and \
    len(tweet['statuses']) > 500

# # Loop through all target users
for user in target_terms:
#     # Variables for holding sentiments
    compound_list = []
    positive_list = []
    negative_list = []
    neutral_list = []

#     # Loop through 10 times (total of 1500 tweets)
    for page in tweepy.Cursor(api.user_timeline, id=user).pages(1):
        # Loop through all tweets
        for tweet in page:

            tweet_text = json.dumps(tweet._json, indent=3)
            tweet = json.loads(tweet_text)
            print(tweet['text'])

#             # Use filters to check if user meets conditions


#                 # Run Vader Analysis on each tweet
#                 # Run analysis
#                 raise NotImplementedError()

#                 # Add each value to the appropriate array
#                 # YOUR CODE HERE
#                 raise NotImplementedError()

#     # Store the Average Sentiments
#     # YOUR CODE HERE
#     raise NotImplementedError()

#     # Print the Sentiments
#     # YOUR CODE HERE
#     raise NotImplementedError()
