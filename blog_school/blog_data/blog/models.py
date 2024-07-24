from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    author = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.title}, {self.author}'
