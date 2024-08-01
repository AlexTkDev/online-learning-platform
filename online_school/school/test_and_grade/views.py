from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import Tests, Grades
from courses.serializers import CourseSerializer
from .serializers import GradesSerializer


# Tests =================================================================


class CourseListAPIView(generics.ListAPIView):
    queryset = Tests.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated]


class CourseDetailAPIView(generics.ListCreateAPIView):
    queryset = Tests.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated]


class CourseRetriveUpdateDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tests.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated]


# Grades =================================================================


class GradeListAPIView(generics.ListAPIView):
    queryset = Grades.objects.filter(pk__in=Grades.objects.values_list('pk', flat=True))
    serializer_class = GradesSerializer
    permission_classes = [IsAuthenticated]


