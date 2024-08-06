from rest_framework import generics
from blog.models import Post
from blog.serializers import PostSerializer


class PostList(generics.ListAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()


class CreatePost(generics.CreateAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
