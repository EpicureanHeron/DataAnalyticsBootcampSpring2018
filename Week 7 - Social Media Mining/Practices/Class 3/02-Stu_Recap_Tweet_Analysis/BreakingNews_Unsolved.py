# Dependencies
import tweepy
import json
import numpy as np
import config

# Import and Initialize Sentiment Analyzer
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
analyzer = SentimentIntensityAnalyzer()

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
target_term = "@CNNbrk"

# Add List to hold sentiment
user_compound_list = []
user_positive_list = []
user_neutral_list = []
user_negative_list = []

# Grab 25 tweets &
# Loop through all tweets
for tweet in tweepy.Cursor(api.user_timeline, id=target_term).items(25):
    tweet_text = json.dumps(tweet._json, indent=3)
    tweet = json.loads(tweet_text)
    target_string = tweet['text']

    #  Run Vader Analysis on each tweet
    user_compound = analyzer.polarity_scores(target_string)["compound"]
    user_pos = analyzer.polarity_scores(target_string)["pos"]
    user_neu = analyzer.polarity_scores(target_string)["neu"]
    user_neg = analyzer.polarity_scores(target_string)["neg"]
   
    #  Add each value to the appropriate array
    user_compound_list.append(user_compound)
    user_positive_list.append(user_pos)
    user_neutral_list.append(user_neu)
    user_negative_list.append(user_neg)
  
# Store the Average Sentiments
avg_comp = np.mean(user_compound_list)
avg_pos = np.mean(user_positive_list)
avg_neu = np.mean(user_neutral_list)
avg_neg = np.mean(user_negative_list)

# Print the Sentiments
print("Average Compound: " + str(avg_comp))
print("Average Positive: " + str(avg_pos))
print("Average Neutral: " + str(avg_neu))
print("Average Negative: " + str(avg_neg))

