from rest_framework import generics
from blog.models import Post
from blog.serializers import PostSerializer


class PostList(generics.ListAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.filter(is_published=True).order_by('-updated')


class CreatePost(generics.CreateAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()


class UpdatePost(generics.RetrieveUpdateAPIView):
    http_method_names = ['put', 'patch', 'post', 'get']
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
