from django.db import models

from social_rss.modules.twitterfetcher import TwitterFetcher

class Users(models.Model):
    username           = models.CharField(max_length = 30)
    youtube_id         = models.CharField(max_length = 30, blank = True, null = True)
    twitter_id         = models.CharField(max_length = 30, blank = True, null = True)
    instagram_id       = models.CharField(max_length = 30, blank = True, null = True)
    facebook_id        = models.CharField(max_length = 30, blank = True, null = True)
    
    def __repr__(self):
        return {
            'username': self.username,
            'Youtube': self.youtube_id,
            'Twitter': self.twitter_id,
            'Instagram': self.instagram_id,
            'Facebook': self.facebook_id
        }

class Posts(models.Model):
    user_id         = models.ForeignKey(Users, on_delete=models.CASCADE)
    original_id     = models.CharField(max_length = 30)
    title           = models.CharField(max_length = 120)
    content         = models.TextField(blank = True, null = True)
    thumb           = models.CharField(max_length = 120, blank = True, null = True)
    link            = models.CharField(max_length = 120)
    published       = models.DateField()
    origin          = models.CharField(max_length = 20)
    
    


    
# newPost = Posts(original_id = 'Rkynn7ify5s', title = a['Rkynn7ify5s']['title'], content = a['Rkynn7ify5s']['description'], thumb = a['Rkynn7ify5s']['thumbnail'], link = a['Rkynn7ify5s']['link'], published = a['Rkynn7ify5s']['published'], origin = 'Youtube')


# class TwitterPosts(models.Model):
#     title           = models.CharField(max_length = 120)
#     description     = models.TextField(blank = True, null = True)
#     thumb           = models.CharField(max_length = 120, blank = True, null = True)
#     link            = models.CharField(max_length = 120)
#     published       = models.DateField()                                   
    
# 'title': entry.title,
# 'description': entry.description,
# 'thumbnail': entry.media_thumbnail[0]['url'],
# 'link': entry.link,
# 'published': entry.published

# from social_rss.models import Posts
# from social_rss.modules import youtubefetcher
# yt = youtubefetcher.YoutubeFetcher("FramestoerOfficial")