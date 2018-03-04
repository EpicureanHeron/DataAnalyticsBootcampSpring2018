# Dependencies
import pandas as pd
import tweepy
import time
import json
import random
import config

# Twitter API Keys
consumer_key = config.consumer_key
consumer_secret = config.consumer_secret
access_token = config.access_token
access_token_secret = config.access_token_secret

# auth tweepy
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())

# Quotes to Tweet
happy_quotes = [
    "For every minute you are angry you lose sixty seconds of happiness. - Ralph Waldo Emerson",
    "Folks are usually about as happy as they make their minds up to be. - Abraham Lincoln",
    "Happiness is when what you think, what you say, and what you do are in harmony. - Mahatma Gandhi",
    "Count your age by friends, not years. Count your life by smiles, not tears. - John Lennon",
    "Happiness is a warm puppy. - Charles M. Schulz",
    "The happiness of your life depends upon the quality of your thoughts. - Marcus Aurelius",
    "Now and then it's good to pause in our pursuit of happiness and just be happy. - Guillaume Apollinaire"]

# Create function for tweeting
def tweet(status):
    api.update_status(status)
# Twitter credentials
tweet_count = 0
while(tweet_count <7):
    # Tweet a random quote
    status = happy_quotes[random.choice(happy_quotes))]
    # Print success message
    try:
        tweet(status)
        print("Tweet sent")
        tweet_count += 1
    except:
        print("Failed to tweet")
    # Set timer to run every minute
    time.sleep(60)