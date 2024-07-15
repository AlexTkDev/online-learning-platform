from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = models.CharField(max_length=50),
    last_name = models.CharField(max_length=50),
    first_name = models.CharField(max_length=50),
    role = models.CharField(max_length=50),  # teacher of student
    email = models.EmailField(),
    password = models.CharField(max_length=120),

    def __str__(self):
        return f"User: {self.username}"
