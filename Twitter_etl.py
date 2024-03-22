import tweepy
import pandas as pd
import json
from datetime import datetime
import s3fs
from dotenv import load_dotenv
import os 
load_dotenv()

access_key = os.getenv('Twitter_API_Key')
access_secret = os.getenv('Twitter_API_secret_Key')
consumer_key = os.getenv('Access_Token ')
consumer_secret = os.getenv('Access_Token_secret')


# authentication for access
#authorization= tweepy.OAuthHandler(access_key,access_secret)
#authorization.set_access_token(consumer_key, consumer_secret)

bearer_token = "AAAAAAAAAAAAAAAAAAAAAFjBswEAAAAAMLsp%2FJemH7GeBETwFYIPHP5y9HY%3DuKJLGhJffm8c7TyGtCojkXPe1JTDwRrpMWLQOg1SpFZAVVJYdy"
auth = tweepy.AppAuthHandler(consumer_key,consumer_secret)

#API object
#api = tweepy.API(authorization)
api = tweepy.API(auth)
#extracting tweets
tweets = api.user_timeline(screen_name='@NVIDIAAI',
                           # num of tweets to extract
                           count = 100,
                           include_rts = False, 
                           # no retweets
                           # for full length of tweet
                           tweet_mode = 'extended'
                           )

print(tweets)
