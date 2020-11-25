from django.db.models.base import Model
from django.forms import ModelForm
from .models import Post


class MyPostForm(ModelForm):
    class Meta:
        model = Post
        fields = [ 'title', 'text', 'author']