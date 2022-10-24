from django.urls import path, include
from .views import hello_world, some_tests

urlpatterns = [
    path('', hello_world),
    path('testy/', some_tests)
]
