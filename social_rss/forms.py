from django import forms

from .models import Users

class UsersModelForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = [
            "username",
            "youtube_id",
            "twitter_id",
            "instagram_id",
            "facebook_id"
        ]