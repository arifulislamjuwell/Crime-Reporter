from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Crimerepost(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name= models.CharField(max_length=10)
    phone=models.CharField(max_length=12,blank=True)
    district=models.CharField(max_length=20)
    location=models.CharField(max_length=30)
    message=models.TextField(max_length=200)
    date=models.DateField(blank=True, auto_now_add=True)
    is_instant=models.BooleanField(default=True)

    def __str__(self):
        return self.name 