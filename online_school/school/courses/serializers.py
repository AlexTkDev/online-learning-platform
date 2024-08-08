from rest_framework import serializers
from courses.models import Course
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        ref_name = 'CourseUserSerializer'
        fields = ['id', 'username', 'first_name', 'last_name']


class CourseSerializer(serializers.ModelSerializer):
    students = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = ['course_name', 'teacher_name', 'students', 'start_date']
