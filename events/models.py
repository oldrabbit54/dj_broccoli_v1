import datetime

from django.contrib.auth.models import User
from django.db import models

class Category(models.Model):
    cat = models.CharField(max_length=20)
    color = models.CharField(max_length=20)
    def __str__(self):
        return self.cat.title()
class EventModel(models.Model):
    title = models.CharField(max_length=20)
    body = models.TextField(blank=False)
    cat = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='event', default=3)
    time_create = models.DateTimeField(auto_now_add=True)#UTC
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='event')
    expire_time = models.DateField()
    expire_time_hours = models.TimeField()

    def __str__(self):
        return f'{self.title}, category: {self.cat.cat}, at: {self.time_create}'