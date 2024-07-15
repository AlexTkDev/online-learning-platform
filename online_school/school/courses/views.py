from rest_framework import generics
from courses.models import Course
from courses.serializers import CourseSerializer


class CourseList(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class RetriveUpdateDestroyCoursesAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
