from django.shortcuts import render
from .models import Post


def post_details(request, post_id):
    post = Post.objects.get(pk=post_id)
    context = {'post_details': post}

    return render(request, "posts/details.html", context)
    
def posts_list(request):
    posts = Post.objects.all()
    context = {'posts_list': posts}

    return render(request, "posts/list.html", context)

