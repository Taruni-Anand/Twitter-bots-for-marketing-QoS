import tweepy
import json
from pymongo import MongoClient
from textblob import TextBlob

#variable used for accessing positive product tweeters
screen_names = []

consumer_key = ''
consumer_secret = ''
access_token = ''
access_secret = ''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

MONGO_HOST= 'mongodb://localhost/twitterdb'

client = MongoClient(MONGO_HOST)

db = client.twitterdb

tweets_iterator = db.collection.find().limit(100)
for tweet in tweets_iterator:
  text=tweet['text']
  text_data=TextBlob(text)
  print text + "\n"
  print text_data.sentiment
  print "\n"

  #getting positive tweeters
  if text_data.sentiment.polarity > 0:
  	screen_names.append("@" + tweet['user']['screen_name'])

print(screen_names)

myfile = open("screenNames.txt","w")
for name in screen_names:
	myfile.writelines(name+"\n")

myfile.close()

