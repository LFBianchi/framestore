from django.contrib import admin
from django.urls import path, include

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # social_rss
    path('social-rss/', include('social_rss.urls')),
]

urlpatterns += staticfiles_urlpatterns()