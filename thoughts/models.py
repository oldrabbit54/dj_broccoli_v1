from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.db import models
import datetime
from my_profile.models import ProfileModel


class NoteModel(models.Model):
    header = models.CharField(max_length=30, validators=[MinLengthValidator(1)])
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    note = models.TextField(max_length=1000)
    author = models.ForeignKey(ProfileModel, on_delete=models.SET_NULL, related_name='author', null=True)
    def __str__(self):
        return f'\"{self.header}\" by {self.author.first_name}'


class CommentModel(models.Model):
    text = models.TextField(max_length=200)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(ProfileModel, on_delete=models.SET_NULL, related_name='authors', null=True)
    note = models.ForeignKey(NoteModel, on_delete=models.SET_NULL, related_name='notes', null=True)