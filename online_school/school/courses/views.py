from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, BasePermission
from rest_framework.views import APIView
from courses.models import Course
from courses.serializers import CourseSerializer
from users.models import User
from users.enums import Role


# Доступ только для преподавателя и админа
class IsTeacherOrAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.role in [Role.Teacher.name, request.user.is_superuser]


class CourseListAPIView(generics.ListAPIView):
    queryset = Course.objects.all().prefetch_related(
        'students')  # для предварительной загрузки связанных объектов "многие ко многим"
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
            # Получаю курс по его идентификатору (course_id)
            course = Course.objects.prefetch_related('students').get(pk=course_id)
            # Получаем пользователя по его идентификатору (user_id)
            user = User.objects.get(pk=user_id)

            if user.role == Role.Student.name:
                # Добавляю студента в список студентов курса
                course.students.add(user)
                # Возвращаю успешный ответ
                return Response(
                    {"status": "success", "message": "Student added to the course"},
                    status=status.HTTP_200_OK)
            else:
                # Если пользователь не студент, возвращаю ошибку
                return Response({"status": "error", "message": "User is not a student"},
                                status=status.HTTP_400_BAD_REQUEST)
        except Course.DoesNotExist:
            # Если курс не найден, возвращаю ошибку
            return Response({"status": "error", "message": "Course not found"},
                            status=status.HTTP_404_NOT_FOUND)
        except User.DoesNotExist:
            # Если пользователь не найден, возвращаю ошибку
            return Response({"status": "error", "message": "User not found"},
                            status=status.HTTP_404_NOT_FOUND)
