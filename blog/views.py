from django.shortcuts import render

from .models import Post

# Create your views here.


def index(request):
    posts = Post.objects.all().order_by('-date_posted')
    

    return render(request, "blog/index.html", {"posts": posts})



def about(request):
    return render(request, "blog/about.html")