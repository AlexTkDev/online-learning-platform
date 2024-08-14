from rest_framework import serializers
from courses.models import Course
from users.models import User
from users.enums import Role


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        ref_name = 'CourseUserSerializer'
        fields = ['id', 'username', 'first_name', 'last_name']


class CourseSerializer(serializers.ModelSerializer):
    students = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.filter(role=Role.Student.name),
        many=True,
        required=False
    )

    class Meta:
        model = Course
        fields = ['course_name', 'teacher_name', 'students', 'start_date']
