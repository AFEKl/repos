from django.db import models

# Create your models here.
class Post(models.Model):
    Title = models.CharField(max_length=55)
    text = models.TextField()
    img = models.ImageField(upload_to='blog/img/')
    likes = models.PositiveIntegerField(default=0)
    dislikes = models.PositiveIntegerField(default=0)
    draft = models.BooleanField(default=True)
    time_published = models.DateTimeField(auto_now_add=True)
    