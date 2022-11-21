from django.db import models
from django.contrib.auth.admin import User

class Post(models.Model):
    title = models.CharField(max_length=100, default='')
    short_content = models.CharField(max_length=255, default='')
    content = models.TextField(max_length=3000, default='')
    date_published = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="posts", null=True, blank=True)
    author = models.TextField(max_length=150, default='', null=True)

    def __str__(self):
        return f"id:{self.id}, title:{self.title}, short_content:{self.short_content}"

