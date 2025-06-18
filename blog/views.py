from django.shortcuts import render
from .models import Post

def home(request):
    posts = Post.objects.filter(published=True)
    return render(request, 'blog/home.html', {'posts': posts})
