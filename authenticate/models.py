from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user= models.OneToOneField(User, on_delete=models.CASCADE, related_name="messages")
    fullname= models.CharField(max_length=100)
    type_of=models.CharField(max_length=100)
    district=models.CharField(max_length=20)
    phone=models.CharField(max_length=20)
    position=models.CharField(max_length=10)
    
    def __str__(self):
        return self.fullname

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user= instance)