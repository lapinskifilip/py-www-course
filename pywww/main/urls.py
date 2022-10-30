from django.urls import path, include
from .views import homepage, some_tests, about

app_name = "main"
urlpatterns = [
    path('', homepage, name="homepage"),
    path('about', about, name="about"),
    path('testy', some_tests, name="testy")
]
