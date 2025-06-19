from django.shortcuts import render
from .models import Post

def home(request):
    posts = Post.objects.filter(published=True)
    print("Did the full cloning and solving issues of infinity job site")
    print("Attended a long meeting with the team to discuss project UI and UX")
    return render(request, 'blog/home.html', {'posts': posts})
