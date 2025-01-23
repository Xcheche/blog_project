from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post

# Create your views here.


# def index(request):
#     posts = Post.objects.all().order_by('-date_posted')
    

#     return render(request, "blog/index.html", {"posts": posts})

class PostListView(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    #paginate_by = 3


# Detail page


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'  # uses object name by default
    context_object_name = 'post'

def about(request):
    return render(request, "blog/about.html")