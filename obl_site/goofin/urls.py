from django.urls import path
from goofin.views import goof_list_view

urlpatterns = [
    path('', goof_list_view, name="blog_index")
]