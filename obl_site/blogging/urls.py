
from django.urls import path, include
from blogging.views import Form_post, list_view, detail_view, UserViewSet, GroupViewSet, PostsViewSet, CategoryViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'posts', PostsViewSet)
router.register(r'catty', CategoryViewSet)

urlpatterns = [
    path('', list_view, name="blog_index"),
    path('posts/<int:post_id>/', detail_view, name="blog_detail"),
    path('api/', include(router.urls)),
    path('form_post/', Form_post, name="I am bullshitting")
]