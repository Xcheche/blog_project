from django.urls import path

from . import views
from .views import PostListView, PostDetailView

app_name = "blog"
urlpatterns = [
    path("", PostListView.as_view(), name="home"), # PostListView.as_view() is a class-based view
    path("post/<int:pk>/", PostDetailView.as_view(), name="post_detail"),  # pk is the primary key of the post
    path("about/", views.about, name="about"),
]