import datetime

from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator
from django.db import models

from my_profile.models import ProfileModel


# Create your models here
class HelpModel(models.Model):
    author = models.ForeignKey(ProfileModel, on_delete=models.SET_NULL, null=True, related_name='help_author')
    date = models.DateTimeField(auto_now_add=True)
    note = models.TextField(max_length=1000)


class SessionToken(models.Model):
    vk_auth_token = models.CharField(max_length=255)
    token_creation_date = models.DateTimeField(auto_now_add=True)
    vk_user_id = models.CharField(max_length=50, blank=True)
    user = models.OneToOneField(User, on_delete=models.SET_NULL,
                                related_name='vk_profile', null=True, blank=True)
