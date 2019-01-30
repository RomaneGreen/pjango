from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.db.models.signals import post_save



class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=500)
    about = models.CharField(max_length=1000)
    tokens = models.IntegerField(default=0)

    def __str__(self): return self.name

def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)



class TokenTransfer(models.Model):
    sender = models.ForeignKey(UserProfile,on_delete=models.CASCADE, related_name="sender")
    message = models.CharField(max_length=1000)
    tokens = models.IntegerField(default=5)
    reciever = models.ForeignKey(UserProfile,on_delete=models.CASCADE, related_name="reciever")
    transfer_time = models.DateTimeField(default=timezone.now)


    