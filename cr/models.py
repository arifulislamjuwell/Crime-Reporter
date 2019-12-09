from django.db import models
from django.contrib.auth.models import User
from authenticate.models import Profile

# Create your models here.
class Crimerepost(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name= 'post_creator')
    name= models.CharField(max_length=50)
    phone=models.CharField(max_length=12, blank=True)
    district=models.CharField(max_length=20)
    location=models.CharField(max_length=30)
    message=models.TextField(max_length=200)
    date=models.DateField(blank=True, auto_now_add=True)
    is_instant=models.BooleanField(default=True)
    refer_user=models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True ,related_name='refer_user')
    take_under=models.ForeignKey(Profile,  on_delete=models.CASCADE, null=True, blank=True ,related_name='take_under')
    is_solved=models.BooleanField(default=False)
    
    def __str__(self):
        return self.name 

class Comment(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    name= models.ForeignKey(Crimerepost, on_delete=models.CASCADE)
    body=models.CharField(max_length=1000)
    cerated_time=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body 