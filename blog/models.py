from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Blog(models.Model):
    auth_name = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_date = models.DateField(auto_now_add=True)
    likes = models.IntegerField(default=0)

    def __str__(self) :
        return self.title
    
class Likes(models.Model):
    user = models.ForeignKey(User,related_name='like',on_delete=models.CASCADE)
    post = models.ForeignKey(Blog,related_name='like',on_delete=models.CASCADE)

