"""
Created on Fri Oct 25 21:51:08 2017
@author: Devin Suttles

"""
import wolframalpha
import tweepy   


with open("newton.txt", "r") as newtonsMind:
    array = []
    for quote in newtonsMind:
        array.append(quote)

#override tweepy.StreamListener to add logic to on_status
class MyStreamListener(tweepy.StreamListener):
    consumer_key = "#key"
    consumer_secret = "#secret" 
    access_token = "#accessToken"
    access_secret = "accessTokenSecret"
    wolf_ID="#"

    def __init__(self):
        auth = tweepy.OAuthHandler(MyStreamListener.consumer_key, MyStreamListener.consumer_secret)
        auth.set_access_token(MyStreamListener.access_token, MyStreamListener.access_secret)
        self.api = tweepy.API(auth)
        
        self.client = wolframalpha.Client(MyStreamListener.wolf_ID)
        self.index = 3
    
    def on_status(self, status):
        #increment through the quotes
        self.index +=  1
        if self.index == 5:
            self.index = 0
        
        errorQuote = array[self.index];
        print(status.text[11:])
        try:
            if status.text[11:] != "":#In case twitter user gives empty tweet
                res = self.client.query(status.text[11:])
                try:
                    try:
                        first = next(res.results, None)
                    except AttributeError:
                            print("Attribute Error from " +status.user.screen_name)
                            # pass
                            self.api.update_status("@" + status.user.screen_name + " " + errorQuote, status.id)
                    if first:
                        try:
                            self.api.update_status("@" + status.user.screen_name + " " + first.text, status.id)
                        except Exception:
                            print("Exception Error from " + status.user.screen_name)
                            # pass
                            self.api.update_status("@" + status.user.screen_name + " " + errorQuote, status.id)
                except UnboundLocalError:
                    print("UnboundLocalError from " + status.user.screen_name)
                    # pass
                    self.api.update_status("@" + status.user.screen_name + " " + errorQuote, status.id)
        except tweepy.TweepError:
            print("TweepError: Probably duplicate error")
            # pass
    def on_error(self, status_code):
        if status_code == 420:
            #returning False in on_data disconnects the stream
            return False
        
myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = myStreamListener.api.auth, listener=myStreamListener)

myStream.filter(track=['@Ask_Newton'])
myStream.userstream(_with = "users")



