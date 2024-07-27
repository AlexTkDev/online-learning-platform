from django.urls import path
from courses.views import (RetriveUpdateDestroyCoursesAPIView,
                           CourseListAPIView,
                           CreateCourseAPIView,
                           AddStudentToCourseAPIView,
                           )

urlpatterns = [
    path('', CourseListAPIView.as_view(), name='course-list'),
    path('create/', CreateCourseAPIView.as_view(), name='course-create'),
    path('course/<int:pk>/', RetriveUpdateDestroyCoursesAPIView.as_view(), name='course'),
    path('courses/<int:course_id>/add_student/<int:user_id>/', AddStudentToCourseAPIView.as_view(),
         name='add-student-to-course'),

]
