from django.db.models.base import Model
from django.forms import ModelForm
from .models import Post
from django import forms
# from django.utils import timezone


# https://www.youtube.com/watch?v=VOddmV4Xl1g
class PostForm(ModelForm):
    # published_date = forms.DateField(widget=forms.HiddenInput(), initial=timezone.now())
    class Meta:
        model = Post
        fields = [ 'title', 'text', 'author', 'published_date']
