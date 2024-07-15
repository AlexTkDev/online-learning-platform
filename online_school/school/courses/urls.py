from django.urls import path
from courses.views import RetriveUpdateDestroyCoursesAPIView, CourseList

urlpatterns = [
    path('courses/', CourseList.as_view(), name='course-list'),
    path('course/<int:pk>/', RetriveUpdateDestroyCoursesAPIView.as_view(), name='course'),
]