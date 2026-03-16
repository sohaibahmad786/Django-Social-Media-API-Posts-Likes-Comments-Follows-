from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.conf import settings



# _________________________ Register ________________________
class Register(AbstractUser):
    class Meta:
        verbose_name = "Register"          
        verbose_name_plural = "Register"
        
# _____________________ Social Media API __________________________
class Posts(models.Model):
    author=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='posts')
    content=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.author.username}:{self.content[:20]}"
    
class Comments(models.Model):
    post=models.ForeignKey(Posts,on_delete=models.CASCADE,related_name='comments')
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    text=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}:{self.text[:20]}"
    
class Likes(models.Model):
    post=models.ForeignKey(Posts,on_delete=models.CASCADE,related_name='likes')
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    
    class Meta:
        unique_together=('post','user')

class Follow(models.Model):
    follower=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='following')
    following=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='followers')

    class Meta:
        unique_together=('follower','following')
# Create your models here.
