from django.urls import path

from . import views
from .views import (PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView)


urlpatterns = [
    path("post/new/", views.PostCreateView.as_view(), name="post-create"),
    path("post/<int:pk>/update/", views.PostUpdateView.as_view(), name="post-update"),
    path("post/<int:pk>/delete/", views.PostDeleteView.as_view(), name="post-delete"),
    path("", PostListView.as_view(), name="home"), # PostListView.as_view() is a class-based view
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'), # PostDetailView.as_view() is a class-based view
    path("about/", views.about, name="about"),
]