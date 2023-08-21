from django.core.validators import MinLengthValidator
from django.db import models

class GalleryStorageModel(models.Model):
    image = models.FileField(upload_to='gallery')
    #image = models.FileField(upload_to='../gallery')
    author = models.CharField(max_length=30, validators=[MinLengthValidator(3)])
    date = models.DateTimeField(null=True)
    title = models.CharField(max_length=100, validators=[MinLengthValidator(1)], null=True)