from django.utils.timezone import timedelta, now
from django.db import models
from django.contrib.auth.models import User


class CheckAgeMixin:
    def is_older_than_n_days(self, n=1):
        delta = timedelta(days=n)
        return now() - self.created > delta


class TimeStamped(models.Model, CheckAgeMixin):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Post(TimeStamped):
    title = models.CharField(max_length=255)
    content = models.TextField()
    published = models.BooleanField(default=False)
    sponsored = models.BooleanField(default=False)

    author = models.ForeignKey(
        "auth.User", on_delete=models.CASCADE, related_name="posts"
    )

    tags = models.ManyToManyField("tags.Tag", related_name="posts")

    category = models.ManyToManyField("Category", related_name="posts")

    def __str__(self):
        return f"{self.id} - {self.title}"


class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return f"{self.name} - {self.description}"
