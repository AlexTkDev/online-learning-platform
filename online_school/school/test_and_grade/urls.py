from django.urls import path
from .views import CourseListAPIView, CourseDetailAPIView, CourseRetriveUpdateDetailAPIView, GradeListAPIView

urlpatterns = [
    path('', CourseListAPIView.as_view(), name='course-list'),
    path('create/', CourseDetailAPIView.as_view(), name='course-detail'),
    path('update/<int:pk>/', CourseRetriveUpdateDetailAPIView.as_view(), name='course-retrive-update'),
    path('grade/<int:pk>/', GradeListAPIView.as_view(), name='grade-list'),
]