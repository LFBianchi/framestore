from django.urls    import path

from .views import posts_list, UsersCreateView


app_name = "social_rss"
urlpatterns = [   
    # social_rss views
    path('<slug:user>/', posts_list, name = "posts-list"),
    path('setup/create/', UsersCreateView.as_view(), name = "users-create"),
]