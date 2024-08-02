from django.db import models

# Create your models here.
class User(models.Model):
 name = models.TextField(unique=True)
 email = models.TextField(unique=True)
 date = models.DateField()
 password = models.TextField()