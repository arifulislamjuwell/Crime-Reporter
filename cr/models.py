from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Crimerepost(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name= models.CharField(max_length=10)
    phone=models.CharField(max_length=20)
    district=models.CharField(max_length=20)
    location=models.CharField(max_length=30)
    message=models.TextField(max_length=200)

    def __str__(self):
        return self.name 