from django.shortcuts import render
from django.views.generic import ( ListView, DetailView, CreateView, UpdateView, DeleteView )
from .models import Post
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin , UserPassesTestMixin

# Create your views here.


# def index(request):
#     posts = Post.objects.all().order_by('-date_posted')
    

#     return render(request, "blog/index.html", {"posts": posts})

class PostListView(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 3

# Detail page


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'  # uses object name by default
    context_object_name = 'post'

# About page

def about(request):
    return render(request, "blog/about.html")



# CreateView

class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    template_name = 'blog/post_form.html'
    fields = ['title', 'content']

    def form_valid(self, form): # Django cbv view without form dosent require save=false
        form.instance.author = self.request.user  # Set the author to the current logged in user
         # Add success message
        messages.success(self.request, "Your post has been successfully created!")

        return super().form_valid(form)
       
    def get_success_url(self):
        return self.object.get_absolute_url()  # Use the post's absolute URL (the detail page URL)

# UpdateView


class PostUpdateView(LoginRequiredMixin,UpdateView):
    model = Post
    template_name = 'blog/post_form.html'
    fields = ['title', 'content']

    def form_valid(self, form): # Django cbv view without form dosent require save=false
        form.instance.author = self.request.user  # Set the author to the current logged in user
         # Add success message
        messages.success(self.request, "Your post has been successfully updated!")

        return super().form_valid(form)
       
    def get_success_url(self):
        return self.object.get_absolute_url()  # Use the post's absolute URL (the detail page URL)
    
    def test_func(self): # Check if the current user is the author of the post
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


# DeleteView

class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = '/'  # Redirect to the home page after deleting the post

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Your post has been successfully deleted!")
        return super().delete(request, *args, **kwargs)

    def test_func(self):  # Check if the current user is the author of the post
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
