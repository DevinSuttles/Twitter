"""
Created on Fri Oct 25 21:51:08 2017
@author: Devin Suttles
"""
import wolframalpha
import tweepy     

#Use your keys
consumer_key = ""#account.key
consumer_secret = ""#account.secret 
access_token = ""#account.accessToken
access_secret = ""#account.accessTokenSecret
wolf_ID="" #wolfram alpha app id


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

client = wolframalpha.Client(wolf_ID)

#override tweepy.StreamListener to add logic to on_status
class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        print(status.text[11:])
        res = client.query(status.text[11:])
        first = next(res.results, None)
        if first:
            api.update_status(".@" + status.user.screen_name + " " + first.text, status.id)
        
    def on_error(self, status_code):
        if status_code == 420:
            #returning False in on_data disconnects the stream
            return False
        
myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener=MyStreamListener())

myStream.filter(track=['@Ask_Newton'])
myStream.userstream(_with = "users")
