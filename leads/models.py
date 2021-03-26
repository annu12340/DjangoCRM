from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    is_organisor = models.BooleanField(default=True)
    is_agent = models.BooleanField(default=False)


class Lead(models.Model):
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    age=models.IntegerField(default=0)
    agent=models.ForeignKey("Agent",on_delete=models.CASCADE)
    # phoned=models.BooleanField(default=False)
    # source=models.CharField(choices=( ('YT','Youtube'), ('G','Google'),('NL','Newsletter') ),max_length=100)
    # profile_picture=models.ImageField(blank=True,null=True)
    # special_files=models.FileField()

class Agent(models.Model):
    user=models.OneToOneField('User',on_delete=models.CASCADE)

    def __str__(self):
        return self.user.email