from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import Tests, Grades
from courses.serializers import CourseSerializer
from .serializers import GradesSerializer


# Tests =================================================================


class CourseListAPIView(generics.ListAPIView):
    # select_related('test_from_course'):
    # Для модели Tests, это позволяет выполнить JOIN с таблицей Course
    # и получить связанные данные курса в одном запросе.
    queryset = Tests.objects.select_related('test_from_course')
    permission_classes = [IsAuthenticated]


class CourseDetailAPIView(generics.ListCreateAPIView):
    queryset = Tests.objects.select_related('test_from_course')
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated]


class CourseRetriveUpdateDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tests.objects.select_related('test_from_course')
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated]


# Grades =================================================================


class GradeListAPIView(generics.ListAPIView):
    queryset = Grades.objects.select_related('test_name', 'student_name')
    serializer_class = GradesSerializer
    permission_classes = [IsAuthenticated]
