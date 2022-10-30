
from django.shortcuts import render

def homepage(request):
    return render(request, "main/homepage.html", context = {})

def about(request):
    return render(request, "main/about.html", context = {})

def some_tests(request):
    age = 33
    first_name = 'Kacper'
    children = ['Aniela', 'Rozalia', 'Julian']
    programming_languages = {
        'python': 'advanced',
        'php': 'advanced',
        'js': 'intermediate'
    }
    books = set(['Czysty kod', 'PostgreSQL Biblia'])

    return render(request, "main/some_tests.html", context={
        'age': age,
        'first_name': first_name,
        'children': children,
        'programming_languages': programming_languages,
        'books': books
    })