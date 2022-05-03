from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE,null=True,blank=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    username = models.CharField(max_length=200, null=True, blank=True)
    location = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(max_length=500, blank=True, null=True)
    short_intro =  models.CharField(max_length=200, null=True, blank=True)
    bio = models.TextField(blank=True, null=True)
    profile_image = models.ImageField(blank=True, null=True, upload_to='profileImages/', default = 'profileImages/user-default.png')
    social_github = models.CharField(max_length=200, null=True, blank=True)
    social_linkedin = models.CharField(max_length=200, null=True, blank=True)
    social_personal = models.CharField(max_length=200, null=True, blank=True)
    social_youtube = models.CharField(max_length=200, null=True, blank=True)
    social_instgram = models.CharField(max_length=200, null=True, blank=True)
    social_facebook = models.CharField(max_length=200, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)


    def __str__(self):
        return str(self.username)


class Skill(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True , blank=True)
    name = models.CharField(max_length=200 , blank=True, null=True) 
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
 
 
    def __str__(self):
        return str(self.name)

