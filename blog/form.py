from django import forms

from .models import Post

class PostForm(forms.ModelForm): # class that allows us to make a post through site

    class Meta:
        model = Post
        fields = ('title', 'text',)