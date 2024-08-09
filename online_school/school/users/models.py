from django.contrib.auth.models import AbstractUser
from django.db import models
from .enums import Role


class User(AbstractUser):
    username = models.CharField(max_length=50, unique=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    role = models.CharField(max_length=50, choices=[
        (tag.name, tag.value) for tag in Role]
                            )  # teacher, admin or student
    email = models.EmailField()
    password = models.CharField(max_length=120)

    def __str__(self):
        return f"User: {self.username}"
