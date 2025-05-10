from django.shortcuts import render, get_object_or_404
from django.views.generic import ( ListView, DetailView, CreateView, UpdateView, DeleteView )
from .models import Post
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin , UserPassesTestMixin
from django.contrib.auth.models import User
#Calendar
import calendar
from datetime import datetime
from django.db.models import Q


# Create your views here.


# def index(request):
#     posts = Post.objects.all().order_by('-date_posted')
    

#     return render(request, "blog/index.html", {"posts": posts})
# Post list view
class PostListView(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 3
    
    
    # # Search logic
    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     search_query = self.request.GET.get('q', '')  # Get the search query from the 'search' parameter
    #     if search_query != '' and search_query is not None:
    #         queryset = queryset.filter(title__icontains=search_query)  # Filter posts by title containing the search query
    #     return queryset



#WIth htmx
def search(request):
    import time
    time.sleep(2)  # Simulate a delay for the search
    query = request.GET.get('q', '')
    posts = Post.objects.filter(Q(title__icontains=query) | Q(content__icontains=query)).order_by('-date_posted')
    context = {
        'posts': posts,
        'query': query,
    }
    if not posts:
        context['message'] = 'No posts found.'

    return render(request, 'partials/post_list.html', context)





#All posts by a specific user
class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 3

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')





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



def latest_post(request):
    posts = Post.objects.all().order_by('-date_posted')[:3]
    return render(request, "blog/latest_post.html", {"posts": posts})

#Calendar



def calendar_view(request):
    year = datetime.now().year
    month = datetime.now().month
    cal = calendar.HTMLCalendar().formatmonth(year, month)
    return render(request, 'calendar.html', {'calendar': cal})