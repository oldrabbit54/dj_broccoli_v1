import os
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.core.validators import MinLengthValidator
from django.db import models
from broccoli import settings
import PIL
import datetime


# Create your models here.
class ProfileModel(models.Model):
    avatar = models.ImageField(upload_to='avatars/',
                               storage=FileSystemStorage(
                                   location=os.path.join(settings.MEDIA_ROOT, 'avatars'),
                                   base_url=os.path.join(settings.MEDIA_URL, 'avatars/'),
                               ))
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20, blank=True)
    #email = models.EmailField(max_length=20)
    bio = models.TextField(blank=True)
    user = models.OneToOneField(User, on_delete=models.SET_NULL, related_name='my_profile', null=True)
    date = models.DateTimeField(auto_now_add=True)