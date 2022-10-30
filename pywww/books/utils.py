from random import randint
from .models import Book
from faker import Faker

def create_books(n=10):
    fake = Faker('pl_PL')
    for _ in range(n):
        book = Book(
            title = fake.text(randint(10, 30)),
            description = fake.text(randint(100, 200)),
            author = fake.text(randint(10, 30)),
            publication_year = fake.date_time(),
            avaliable=fake.boolean()
        )
        book.save()