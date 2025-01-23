from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-date_posted']
        verbose_name_plural = "Posts"
        
        
    # get absolute url
    
    def get_absolute_url(self):
        return reverse("blog:post_detail", kwargs={"pk": self.pk}) # Used for detail view