from django.shortcuts import render
from .models import Post

def home(request):
    posts = Post.objects.filter(published=True)
    print("Did the full cloning and solving issues of infinity job site")
    return render(request, 'blog/home.html', {'posts': posts})
