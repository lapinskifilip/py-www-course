from django.shortcuts import render
from .models import Book

def books_list(request):
    books = Book.objects.all()
    return render(request, "books/books_list.html", {'books_list': books})

def book_details(request, book_id):
    book = Book.objects.get(pk=book_id)
    return render(request, "books/books_details.html", {'book_details': book})
