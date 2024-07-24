from rest_framework import generics, permissions
from blog.models import Post
from blog.serializers import PostSerializer


class PostList(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = PostSerializer
    queryset = Post.objects.all()


class CreatePost(generics.CreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = PostSerializer
    queryset = Post.objects.all()


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer
