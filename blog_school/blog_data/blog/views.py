from rest_framework import generics
from blog.models import Post
from blog.serializers import PostSerializer


class PostList(generics.ListCreateAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        queryset = Post.objects.all()
        post_id = self.request.query_params.get('id', None)
        if post_id is not None:
            queryset = queryset.filter(id=post_id)
        return queryset


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
