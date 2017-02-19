"""
Created on Fri Oct 25 21:51:08 2017
@author: Devin Suttles
"""
import wolframalpha
import tweepy     

#Use your keys, from Twitter
consumer_key = ""
consumer_secret = ""
access_token = ""
access_secret = ""
wolf_ID=""#Wolfram Alpha App ID


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

client = wolframalpha.Client(wolf_ID)

#override tweepy.StreamListener to add logic to on_status
class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        print(status.text[11:])
        if status.text[11:] != "":#In case twitter user gives empty tweet
            res = client.query(status.text[11:])
            try:
                try:
                    first = next(res.results, None)
                except AttributeError:
                    print "Attribute Error from " +status.user.screen_name
                    pass
                if first:
                    try:
                        api.update_status(".@" + status.user.screen_name + " " + first.text, status.id)
                    except Exception:
                        print "Exception Error from " + status.user.screen_name
                        pass
            except UnboundLocalError:
                print "UnboundLocalError from " + status.user.screen_name
                pass
        
    def on_error(self, status_code):
        if status_code == 420:
            #returning False in on_data disconnects the stream
            return False
        
myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener=MyStreamListener())

myStream.filter(track=['@Ask_Newton'])
myStream.userstream(_with = "users")
