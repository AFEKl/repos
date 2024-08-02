from django.db import models

# Create your models here.
class Video(models.Model):
    title = models.CharField(max_length=55)
    text = models.TextField(null=True,blank=True)
    embed = models.TextField(unique=True)
    likes = models.PositiveIntegerField(default=0, null=True,blank=True)
    dislikes = models.PositiveIntegerField(default=0, null=True,blank=True)
