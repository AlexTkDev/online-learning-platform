from django.db import models

from courses.models import Course
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator

User = get_user_model()


class Tests(models.Model):
    test_name = models.CharField(max_length=100)
    test_description = models.TextField()
    test_body = models.TextField()
    test_date = models.DateField()
    test_created_date = models.DateField(auto_now_add=True)
    test_from_course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.test_name} - {self.test_date}"


class Grades(models.Model):
    test_name = models.ForeignKey(Tests, on_delete=models.CASCADE, related_name='grades')
    grade = models.IntegerField(
        default=0, validators=[MinValueValidator(1), MaxValueValidator(100)]
    )
    student_name = models.ForeignKey(User, on_delete=models.CASCADE, related_name='grades')
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.test_name} - {self.date}"
