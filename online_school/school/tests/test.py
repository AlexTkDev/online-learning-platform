from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model
from courses.models import Course
from users.enums import Role

User = get_user_model()


class CourseCreationTest(APITestCase):

    def setUp(self):
        # Создаем пользователя-преподавателя
        self.teacher_user = User.objects.create_user(
            username='teacher',
            password='password123',
            role=Role.Teacher.name
        )
        # Создаем пользователя-студента
        self.student_user = User.objects.create_user(
            username='student',
            password='password123',
            role=Role.Student.name
        )
        # URL для создания курса
        self.url = reverse('course-create')

    def test_create_course_as_teacher(self):
        self.client.force_authenticate(user=self.teacher_user)
        data = {
            'course_name': 'Test Course',
            'teacher_name': 'Teacher Name',
            'start_date': '2024-08-15',
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Course.objects.count(), 1)
        self.assertEqual(Course.objects.get().course_name, 'Test Course')

    def test_create_course_as_student(self):
        self.client.force_authenticate(user=self.student_user)
        data = {
            'course_name': 'Test Course',
            'teacher_name': 'Teacher Name',
            'start_date': '2024-08-15',
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(Course.objects.count(), 0)
