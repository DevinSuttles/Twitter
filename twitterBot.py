"""
Created on Fri Oct 25 21:51:08 2017
@author: Devin Suttles

"""
import tweepy 

consumer_key = "key" 
consumer_secret = "secret" 
access_token = "access token"
access_secret= "access token secret" 

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

