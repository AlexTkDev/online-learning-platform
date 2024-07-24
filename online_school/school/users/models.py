from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = models.CharField(max_length=50, unique=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    role = models.CharField(max_length=50)  # teacher of student
    email = models.EmailField()
    password = models.CharField(max_length=120)

    def __str__(self):
        return f"User: {self.username}"
