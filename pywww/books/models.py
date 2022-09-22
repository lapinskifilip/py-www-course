from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField()
    publication_year = models.DateField()
    author = models.CharField(max_length=300)
    avaliable = models.BooleanField(default=True)

