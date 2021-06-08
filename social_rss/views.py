from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView

from .models    import Posts, Users
from .forms     import UsersModelForm

from .modules.twitterfetcher import TwitterFetcher
from .modules.youtubefetcher import YoutubeFetcher

class UsersCreateView(CreateView):
    template_name = "users-create.html"
    form_class = UsersModelForm
    queryset = Users.objects.all()
    
def posts_list(req, user):
    # update database here.
    obj = get_object_or_404(Users, username = user)
    queryset = Posts.objects.filter(user_id = obj).order_by("-published")
    update_user(obj, queryset)
    
    # respond to the request here.
    queryset = Posts.objects.filter(user_id = obj).order_by("-published")
    queryset2 = Users.objects.all()
    context = {
        "object_list": queryset,
        "user_list": queryset2
    }
    return render(req, "posts-list.html", context)

def update_user(obj, queryset):
    #Update Youtube
    fetcher = YoutubeFetcher(obj.youtube_id)
    relevant_data = fetcher.get_relevant_data()
    
    updater(obj, queryset, relevant_data, fetcher.tag)
    
    #Update Twitter
    fetcher = TwitterFetcher(obj.twitter_id)
    relevant_data = fetcher.get_relevant_data()
    
    updater(obj, queryset, relevant_data, fetcher.tag)
    
    #Update Instagram
    
    #Update Facebook
    
def updater(obj, queryset, relevant_data, tag):
    """
    Checks each post agains the database and updates it accordingly
    obj: Django model object
    queryset: Django model queryset
    relevant_data: fetcher.get_relevent_data()
    tag: fetcher.tag.
    """
    for item in relevant_data:
        queryset.filter(original_id = item)
        if not queryset.filter(original_id = item):
            newEntry = Posts(
                user_id         = obj,
                original_id     = item,
                title           = relevant_data[item]["title"],
                content         = relevant_data[item]["description"][:277] + '...',
                thumb           = relevant_data[item].get("thumbnail", None),
                link            = relevant_data[item]["link"],
                published       = relevant_data[item]["published"],
                origin          = tag
            )
            newEntry.save()