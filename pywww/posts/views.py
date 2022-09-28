from django.shortcuts import render
from .models import Post

def posts_list(request):
    posts = Post.objects.all()
    context = {'posts_list': posts}

    return render(request, "posts/list.html", context)

