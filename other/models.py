from django.db import models
from django.contrib.auth.models import User
from authenticate.models import Profile

class Notice(models.Model):
    crater= models.ForeignKey(User, on_delete=models.CASCADE)
    area = models.ForeignKey(Profile, on_delete=models.CASCADE)
    title= models.CharField(max_length=50)
    created_time= models.DateField(auto_now=True)
    expire_time=models.DateField(null= True)
    descrp= models.CharField(max_length= 100)
    exact_location= models.CharField(max_length= 100)

    def __str__(self):
        return self.title