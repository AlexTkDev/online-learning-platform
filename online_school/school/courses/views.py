from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from courses.models import Course
from courses.serializers import CourseSerializer
from users.models import User


class CourseListAPIView(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CreateCourseAPIView(generics.CreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class RetriveUpdateDestroyCoursesAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class AddStudentToCourseAPIView(APIView):
    def post(self, request, course_id, user_id):
        try:
            course = Course.objects.get(pk=course_id)
            user = User.objects.get(pk=user_id)
            if user.role == 'student':
                course.students.add(user)
                return Response({"status": "success", "message": "Student added to the course"},
                                status=status.HTTP_200_OK)
            else:
                return Response({"status": "error", "message": "User is not a student"},
                                status=status.HTTP_400_BAD_REQUEST)
        except Course.DoesNotExist:
            return Response({"status": "error", "message": "Course not found"}, status=status.HTTP_404_NOT_FOUND)
        except User.DoesNotExist:
            return Response({"status": "error", "message": "User not found"}, status=status.HTTP_404_NOT_FOUND)
