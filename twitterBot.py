"""
Created on Fri Oct 25 21:51:08 2017
@author: Devin Suttles

"""
import json, account
import ConfigParser 

from tweepy import Stream
from tweepy import OAuthHandler 
from tweepy import Stream 
from tweepy import API 

from nltk.chat import eliza        

config = ConfigParser.ConfigParser() 
config.read('.twitter')

consumer_key = config.get(account.key)
consumer_secret = config.get(account.secret)
access_token = config.get(accounts.accessToken)
access_token_secret = config.get(accounts.accessTokenSecret)
stream_rule = config.get("Practice","r+")
account_screen_name = config.get(account.owner).lower() 
account_user_id = config.get(account.ID)                                

auth = OAuthHandler(account.key, account.secret)
auth.set_access_token(account.accessToken, account.accessTokenSecret)
twitterApi = API(auth)

bot = eliza.Chat(eliza.pairs)   


class ReplyToTweet(StreamListener):

    def on_data(self, data):

        tweet = json.loads(data.strip())
        
        retweeted = tweet.get('retweeted', False)
        from_self = tweet.get('user',{}).get('id_str','') == account_user_id
        mentions_self = self.mentionsSelf(tweet)

        if not retweeted and not from_self and mentions_self:

            tweetId = tweet.get('id_str')
            screenName = tweet.get('user').get('screen_name')
            tweetText = tweet.get('text')

            replyText = '@' + screenName + ' ' + chatbot.respond(tweetText)

            #check if repsonse is over 140 char
            if len(replyText) > 140:
                replyText = replyText[0:137] + '...'

            print('Tweet ID: ' + tweetId)
            print('From: ' + screenName)
            print('Tweet Text: ' + tweetText)
            print('Reply Text: ' + replyText)

            # If rate limited, the status posts should be queued up and sent on an interval
            twitterApi.update_status(replyText, tweetId)


    def on_error(self, status):
        print status


    def mentionsSelf(self, tweet):
        result = False
        user_mentions = tweet.get('entities',{}).get('user_mentions',{})

        for user in user_mentions:
            if user.get('id_str') == account_user_id:
                result = True
        
        return result


if __name__ == '__main__':
    r = ReplyToTweet()
    twitterStream = Stream(auth, r)
    twitterStream.userstream(track=[stream_rule])
