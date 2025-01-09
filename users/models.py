from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=100, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    avatar = models.ImageField(default="default.jpg",upload_to='avatars/', blank=True)
    
    
    
    def __str__(self):
        return self.user.username
    
    
    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'