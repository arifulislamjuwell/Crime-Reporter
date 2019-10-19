from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    fullname= models.CharField(max_length=100)
    type=models.CharField(max_length=100)
