"""
Created on Fri Oct 25 21:51:08 2017
@author: Devin Suttles
"""
import wolframalpha
import tweepy   
import variable  

#Use your keys
consumer_key = ""
consumer_secret = ""
access_token = ""
access_secret = ""
wolf_ID=""#Wolfram Alpha App ID

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)

client = wolframalpha.Client(wolf_ID)

with open("newton.txt", "r") as newtonsMind:
    array = []
    for quote in newtonsMind:
        array.append(quote)

#override tweepy.StreamListener to add logic to on_status
class MyStreamListener(tweepy.StreamListener):
    variable.index = 3
    def on_status(self, status):
        #increment through the quotes
        variable.index +=  1
        if variable.index == 5:#stuff
            variable.index = 0
        
        errorQuote = array[variable.index];
        print(status.text[11:])
        try:
            if status.text[11:] != "":#In case twitter user gives empty tweet
                res = client.query(status.text[11:])
                try:
                    try:
                        first = next(res.results, None)
                    except AttributeError:
                            print "Attribute Error from " +status.user.screen_name
                            pass
                            api.update_status(".@" + status.user.screen_name + " " + errorQuote, status.id)
                    if first:
                        try:
                            api.update_status(".@" + status.user.screen_name + " " + first.text, status.id)
                        except Exception:
                            print "Exception Error from " + status.user.screen_name
                            pass
                            api.update_status(".@" + status.user.screen_name + " " + errorQuote, status.id)
                except UnboundLocalError:
                    print "UnboundLocalError from " + status.user.screen_name
                    pass
                    api.update_status(".@" + status.user.screen_name + " " + errorQuote, status.id)
        except tweepy.TweepError:
            print "TweepError: Probably duplicate error"
            pass
    def on_error(self, status_code):
        if status_code == 420:
            #returning False in on_data disconnects the stream
            return False
        
myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener=MyStreamListener())

myStream.filter(track=['@Ask_Newton'])
myStream.userstream(_with = "users")
