from django.db import models
from posts.models import TimeStamped


class Author(TimeStamped):
    name = models.CharField(max_length=200)
    birth_year = models.IntegerField()
    death_year = models.IntegerField(blank=True, null=True)
    biogram = models.TextField()

    def __str__(self) -> str:
        return f"{self.name} ({self.birth_year}"


class Book(TimeStamped):
    title = models.CharField(max_length=300)
    description = models.TextField()
    publication_year = models.DateField()
    avaliable = models.BooleanField(default=True)

    authors = models.ManyToManyField(Author, related_name="books")
    tags = models.ManyToManyField("tags.Tag", related_name="books")

    def __str__(self) -> str:
        return (
            f"{self.title} {self.description} {self.publication_year} {self.avaliable}"
        )
