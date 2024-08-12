from django.urls import path
from .views import PostListView, PostDetailView, PostUpdateView

urlpatterns = [
    path('', PostListView.as_view(), name='index'),
    path('post-detail/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post-update/<int:pk>/', PostUpdateView.as_view(), name='post-update'),
]
