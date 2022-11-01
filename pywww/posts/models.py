from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    published = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    sponsored = models.BooleanField(default=False)

    author = models.ForeignKey("auth.User",
                               on_delete=models.CASCADE,
                               related_name="posts"
                               )

    tags = models.ManyToManyField("tags.Tag", related_name="posts")

    category = models.ManyToManyField("Category", related_name="posts")

    def __str__(self):
        return f"{self.id} - {self.title}"

class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
