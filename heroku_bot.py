# Dependencies
import tweepy
import json
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random
import time

# Import and Initialize Sentiment Analyzer
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
analyzer = SentimentIntensityAnalyzer()

# Twitter API Keys. Place your keys here.
#from config import api_keyTwitter
#from config import api_secretTwitter
#from config import access_tokenTwitter
#from config import access_tokensecretTwitter

#This is how i hide my API keys in heroku
api_keyTwitter= os.environ['']
pi_secretTwitter= os.environ['']
access_tokenTwitter= os.environ['']
access_tokensecretTwitter= os.environ['']

# Setup Tweepy API Authentication

auth = tweepy.OAuthHandler(api_keyTwitter, api_secretTwitter)
auth.set_access_token(access_tokenTwitter, access_tokensecretTwitter)
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
def HappyItUp():


    # Tweet a random quote
    api.update_status(random.choice(happy_quotes))

    # Print success message
    print("Tweeted successfully, sir!")


# Set timer to run every minute
while(True):
    HappyItUp()
    time.sleep(60)