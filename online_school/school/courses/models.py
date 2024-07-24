from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Course(models.Model):
    course_name = models.CharField(max_length=100)
    teacher_name = models.CharField(max_length=50)
    student_name = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    start_date = models.DateField()

    def __str__(self):
        return self.course_name