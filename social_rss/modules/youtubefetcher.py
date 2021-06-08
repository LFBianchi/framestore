import feedparser
from dateutil import parser

class YoutubeFetcher(object):
    """Expects screen name of the user in the 'user' parameter."""
    def __init__(self, user):
        
        self.tag = "Youtube"
        
        self.feed_handler = {}
        target_url = r"https://www.youtube.com/feeds/videos.xml?user=" + user
        self.yt_feed = feedparser.parse(target_url)
        
        for entry in self.yt_feed.entries:
            self.feed_handler[entry.yt_videoid] = {
                'title': entry.title,
                'description': entry.description,
                'thumbnail': entry.media_thumbnail[0]['url'],
                'link': entry.link,
                'published': parser.parse(entry.published)
            }
    
    def get_relevant_data(self):
        return self.feed_handler
        
if __name__ == "__main__":
    # framestore yt rss feed
    
    goodboy = YoutubeFetcher("FramestoreOfficial")
    for entry in goodboy.get_relevant_data():
        for key in goodboy.feed_handler[entry]:
            print(key + ":" + str(goodboy.feed_handler[entry][key]))
        