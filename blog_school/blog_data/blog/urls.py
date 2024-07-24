from django.urls import path
from blog.views import PostList, PostDetail, CreatePost

urlpatterns = [
    path('', PostList.as_view(), name='post-list'),
    path('create/', CreatePost.as_view(), name='post-create'),
    path('post/<int:pk>/', PostDetail.as_view(), name='post-detail'),
]