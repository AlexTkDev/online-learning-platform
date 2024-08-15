from django.db import models
from django.contrib.auth.models import AbstractUser
from users.enums import Role


class User(AbstractUser):
    username = models.CharField(max_length=50, unique=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    role = models.CharField(
        max_length=50,
        choices=[(role.value, role.value) for role in Role],
        default=Role.Student.value
    )
    email = models.EmailField()
    password = models.CharField(max_length=120)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return f"User: {self.username}"
