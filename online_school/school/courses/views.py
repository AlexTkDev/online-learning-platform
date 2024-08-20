from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, BasePermission
from rest_framework.views import APIView
from courses.models import Course
from courses.serializers import CourseSerializer
from users.models import User
from users.enums import Role


# Access only for teacher and admin
class IsTeacherOrAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.role in [Role.Teacher.name, request.user.is_superuser]


class CourseListAPIView(generics.ListAPIView):
    queryset = Course.objects.all().prefetch_related(
        'students')  # to preload many-to-many related objects
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated]


class CreateCourseAPIView(generics.CreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated, IsTeacherOrAdmin]


class RetriveUpdateDestroyCoursesAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all().prefetch_related('students')
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated, IsTeacherOrAdmin]


class AddStudentToCourseAPIView(APIView):
    permission_classes = [IsAuthenticated, IsTeacherOrAdmin]

    def post(self, request, course_id, user_id):
        try:
            # I get a course by its identifier (course_id)
            course = Course.objects.prefetch_related('students').get(pk=course_id)
            # We get the user by his identifier (user_id)
            user = User.objects.get(pk=user_id)

            if user.role == Role.Student.name:
                # Adding a student to the list of course students
                course.students.add(user)
                # I return a successful response
                return Response(
                    {"status": "success", "message": "Student added to the course"},
                    status=status.HTTP_200_OK)
            else:
                # If the user is not a student, I return an error
                return Response({"status": "error", "message": "User is not a student"},
                                status=status.HTTP_400_BAD_REQUEST)
        except Course.DoesNotExist:
            # If the course is not found, I return an error
            return Response({"status": "error", "message": "Course not found"},
                            status=status.HTTP_404_NOT_FOUND)
        except User.DoesNotExist:
            # Если пользователь не найден, возвращаю ошибку
            return Response({"status": "error", "message": "User not found"},
                            status=status.HTTP_404_NOT_FOUND)
