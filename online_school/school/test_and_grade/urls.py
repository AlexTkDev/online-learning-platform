from django.urls import path
from .views import CourseListAPIView, CourseDetailAPIView, CourseRetriveUpdateDetailAPIView

urlpatterns = [
    path('', CourseListAPIView.as_view(), name='course-list'),
    path('create/', CourseDetailAPIView.as_view(), name='course-detail'),
    path('create/<int:pk>/', CourseRetriveUpdateDetailAPIView.as_view(), name='course-retrive-update'),
]