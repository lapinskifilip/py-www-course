from django.http import HttpResponse

def books_list(request):
    return HttpResponse("/books/ working")
