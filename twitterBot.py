"""
Created on Fri Oct 25 21:51:08 2017
@author: Devin Suttles
"""
import account

import tweepy     

def isWordInString(word, string, matches, index):
    if matches == (len(word)):
        return True
    elif index > (len(string) - 1):
        return False
    elif word[matches] == string[index]:
        return isWordInString(word, string, matches + 1, index + 1)
    elif word[matches] != string[index]:
        return isWordInString(word, string, 0, index + 1)

#Use your keys
consumer_key = "LwI9JtZEFE8JpxDAdTuKJj7cc"#account.key
consumer_secret = "SHm5nXAb0iMZHJF4qPNwSx2WFalLybOFPfNc2ReJ1CkeuidLfD"#account.secret 
access_token = "480036925-UviFhAhHmBz6W0xtn4p5KxSeT5O8ogDKuqUjir0K"#account.accessToken
access_secret = "uxmFiXzeUitAMq0NDDNrpYAwI3rA2z42jyOCHtJOVUJiL"#account.accessTokenSecret


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

public_tweets = api.home_timeline(count = 10)
for tweet in public_tweets:
    print tweet.text
    if isWordInString("@DevinSuttles", tweet.text, 0, 0):
        api.update_status(api.update_status(".@" + tweet.user.screen_name + " Time", tweet.id))#change @Ian Yake to user of tweet
    #print tweet.text


"""
#override tweepy.StreamListener to add logic to on_status
class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        print(status.text)
        
    def on_error(self, status_code):
        if status_code == 420:
            #returning False in on_data disconnects the stream
            return False
        
myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener=MyStreamListener())
"""
