#!/usr/bin/env python
import tweepy, sys, time
import os
from random import randint
from keys import keys

#f = open('screenNames.txt')
#h = f.readlines()
#for i, a in enumerate(h):
    #h[i] = h[i].strip(' \n')
#f.close()
#print h

CONSUMER_KEY = keys['consumer_key']
CONSUMER_SECRET = keys['consumer_secret']
ACCESS_TOKEN = keys['access_token']
ACCESS_TOKEN_SECRET = keys['access_token_secret']

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

h = [u'@ATaruni', u'@anushbaskaran17']

for i in h:
    i = i.rstrip()
    status = i + " " + "! Our New Products Launched at a reasonable price!"
    fn = os.path.abspath('/Users/anushbaskaran/Desktop/Final Year Project/Project_Boots.png')
    api.update_with_media(fn, status=status)
    nap = randint(1, 60)
    time.sleep(nap)