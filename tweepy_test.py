import tweepy
import time
from datetime import datetime

## Authorization tokens: ##

access_token = # A string containing you access tokens here.
access_token_secret = #A string containing your access tokens here.
consumer_key = # A string containing your consumer key here.
consumer_secret = # A string containing your secret consumer key here.

## More Twitter API authorization stuff. ##

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

## Plant-watering function for PySerial. ##

## In short: here's what's going on in the block of code below:
## With each pass of the while-loop, the API grabs the tweets in the bot's
## entire tweet timeline in JSON form. A for-loop checks each string in the
## list using the .text attribute, and checks it for 'Water my plant!'.

## To do: create list of tweet.id_str that have already been used, don't use any
## ID over again.


while True:
   public_tweets = api.home_timeline()
   for tweet in public_tweets:
      if tweet.text == 'Water my plant!':
         print('Water request received.\n')
         update = 'Plant successfully watered on ' + str(datetime.now()) + '.'
         api.destroy_status(tweet.id_str)
         api.update_status(update)
         print('Water successful. Timeline has been updated.\n')
      time.sleep(10)
