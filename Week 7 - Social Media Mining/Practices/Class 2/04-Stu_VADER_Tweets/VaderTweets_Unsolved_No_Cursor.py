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

# Setup Tweepy API Authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())

# Target User Account
target_user = "@Dalailama"
trump_handle = "@realdonaldtrump"

# Variables for holding sentiments
user_compound_list = []
user_positive_list = []
user_neutral_list = []
user_negative_list = []

trump_compound_list = []
trump_positive_list = []
trump_neutral_list = []
trump_negative_list = []


# Loop through 10 pages of tweets (total 200 tweets)
for x in range(10):

    # Get all tweets from home feed
    public_tweets = api.user_timeline(target_user, page=x+1)
    trump_tweets = api.user_timeline(trump_handle, page=x+1)
    # Loop through all tweets
    for tweet in public_tweets:
        target_string = tweet['text']
        # Run Vader Analysis on each tweet
        user_compound = analyzer.polarity_scores(target_string)["compound"]
        user_pos = analyzer.polarity_scores(target_string)["pos"]
        user_neu = analyzer.polarity_scores(target_string)["neu"]
        user_neg = analyzer.polarity_scores(target_string)["neg"]

        # Add each value to the appropriate list
        user_compound_list.append(user_compound)
        user_positive_list.append(user_pos)
        user_neutral_list.append(user_neu)
        user_negative_list.append(user_neg)

    for tweet in trump_tweets:
        target_string = tweet['text']
        # Run Vader Analysis on each tweet
        trump_compound = analyzer.polarity_scores(target_string)["compound"]
        trump_pos = analyzer.polarity_scores(target_string)["pos"]
        trump_neu = analyzer.polarity_scores(target_string)["neu"]
        trump_neg = analyzer.polarity_scores(target_string)["neg"]

        # Add each value to the appropriate list
        trump_compound_list.append(trump_compound)
        trump_positive_list.append(trump_pos)
        trump_neutral_list.append(trump_neu)
        trump_negative_list.append(trump_neg)
        

# Print the Averages
print(target_user + ': ')
print('Average Compound: ' + str(round(sum(user_compound_list) / len(user_compound_list),2)))
print('Average Positive: ' + str(round(sum(user_positive_list) / len(user_positive_list),2)))
print('Average Neutral: ' + str(round(sum(user_neutral_list) / len(user_neutral_list),2)))
print('Average Negative: ' + str(round(sum(user_negative_list) / len(user_negative_list),2)))

print('------------------------------')

# Print the Averages
print(trump_handle + ': ')
print('Average Compound: ' + str(round(sum(trump_compound_list) / len(trump_compound_list),2)))
print('Average Positive: ' + str(round(sum(trump_positive_list) / len(trump_positive_list),2)))
print('Average Neutral: ' + str(round(sum(trump_neutral_list) / len(trump_neutral_list),2)))
print('Average Negative: ' + str(round(sum(trump_negative_list) / len(trump_negative_list),2)))
