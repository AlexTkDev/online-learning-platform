from django.db import models

from courses.models import Course


# Create your models here.

class Tests(models.Model):
    test_name = models.CharField(max_length=100)
    test_description = models.TextField()
    test_body = models.TextField()
    test_date = models.DateField()
    test_created_date = models.DateField(auto_now_add=True)
    test_from_course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.test_name
