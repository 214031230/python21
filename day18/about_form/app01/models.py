from django.db import models


# Create your models here.

class User(models.Model):
    user = models.CharField(max_length=8)
    pwd = models.CharField(max_length=8)
