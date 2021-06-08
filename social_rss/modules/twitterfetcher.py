import tweepy
import json
from dateutil import parser

class TwitterFetcher(object):
    """Expects screen name of the user in the 'user' parameter."""
    def __init__(self, user='twitter'):
        
        self.tag = "Twitter"
        
        with open("static/credentials.json", "r") as credentials:
            tokens = json.load(credentials)

        consumer_key, consumer_secret = tokens['consumer-key'], tokens['consumer-secret']
        access_token, access_token_secret = tokens['oauth-token'], tokens['oauth-token-secret']
        
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)

        self.screen_name = user
        self.twitter = tweepy.API(auth)
        self.user_tweets = self.twitter.user_timeline(screen_name = user,
                                                      tweet_mode = "extended",
                                                      include_rts = False, 
                                                      count = 30)
        
        self.feed_handler = {}
        
        for entry in [status._json for status in self.user_tweets]:
            # Extrating title/description
            if entry["full_text"].startswith("RT"):
                title = entry["full_text"][:entry["full_text"   ].find(":")]
                description = entry["full_text"][entry["full_text"].find(":") + 2:]
            else:
                title = self.screen_name
                description = entry["full_text"]
            # Extrating thumbnail
            # thumbnail = entry["user"]["profile_image_url"]
            
            # Extrating link
            link = r"https://twitter.com/" + self.screen_name + r"/status/" + str(entry["id"])
            # Extrating published
        
            published = parser.parse(entry["created_at"])
            
            self.feed_handler[entry["id"]] = {
                'title': title,
                'description': description,
                'link': link,
                'published': published
            }
                
    def get_relevant_data(self):
        return self.feed_handler
    
if __name__ == "__main__":
    twit = TwitterFetcher("Framestore")
    tweets = twit.get_relevant_data()
    for tweet_id in tweets.keys():
        print(tweet_id)
        for key in tweets[tweet_id].keys():
            print(key, tweets[tweet_id][key], sep=" : ")
    
    # https://twitter.com/Framestore/status/1400846345456570373