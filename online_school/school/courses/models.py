from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Course(models.Model):
    course_name = models.CharField(max_length=100)
    teacher_name = models.CharField(max_length=50)
    students = models.ManyToManyField(User, related_name='courses')
    start_date = models.DateField()

    def __str__(self):
        return self.course_name