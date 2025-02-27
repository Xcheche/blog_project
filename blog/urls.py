from django.urls import path
from django.shortcuts import render
from . import views
from .views import (PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView, calendar_view)


urlpatterns = [
    path("post/new/", views.PostCreateView.as_view(), name="post-create"),
    path("post/<int:pk>/update/", views.PostUpdateView.as_view(), name="post-update"),
    path("post/<int:pk>/delete/", views.PostDeleteView.as_view(), name="post-delete"),
    path("", PostListView.as_view(), name="home"), # PostListView.as_view() is a class-based view
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'), # Post list view for a specific user
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'), # PostDetailView.as_view() is a class-based view
    #About page
    path("about/", views.about, name="about"),
    #Calendar
    path('calendar/', calendar_view, name='calendar'),
    path("latest/", views.latest_post, name="latest"),
]