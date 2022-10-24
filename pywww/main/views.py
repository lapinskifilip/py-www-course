from django.shortcuts import render
from django.http import HttpResponse

def hello_world(request):
    return HttpResponse("Hello World xx")

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