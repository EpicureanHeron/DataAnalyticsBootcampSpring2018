# Dependencies
import tweepy
import time
from config import openweather_api_key, consumer_key, consumer_secret, \
    access_token, access_token_secret


# Twitter credentials
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())

    
# Quotes to Tweet
quote_list = ["If you're not failing, you're playing it safe and not growing as much as you could be."
              "Everything you want is on the other side of fear.",
              "Do one thing every day that scares you.",
              ]


# Create function for tweeting
def quote_it_up(quote):

    # Tweet the next quote
    try:
        print("Tweeting: '" + quote + "'")
        api.update_status(quote)
        print("Tweeted successfully, sir!")
    except:
        print("Unable to tweet ... =(")

# Create a loop that tweets one quote per minute until
# all of the quotes have been tweeted
for quote in quote_list:
    quote_it_up(quote)
    time.sleep(60)
