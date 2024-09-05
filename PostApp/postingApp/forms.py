from django import forms
from .models import Posts


class Post_form(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ['post']
