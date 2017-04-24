import tweepy
import time
## Authorization tokens: ##

access_token = # A string containing you access tokens here.
access_token_secret = #A string containing your access tokens here.
consumer_key = # A string containing your consumer key here.
consumer_secret = # A string containing your secret consumer key here.

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

while True:
   public_tweets = api.home_timeline()
   for tweet in public_tweets:
      if tweet.text == 'Water my plant!':
         print('\nWater request received.\n')
         tweetID = tweet.id_str
         api.destroy_status(tweetID)
         print('Timeline cleared.\n')
      time.sleep(10)
