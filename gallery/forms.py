from django import forms

from gallery.models import GalleryStorageModel


class GalleryStorageForm(forms.ModelForm):
    class Meta:
        model = GalleryStorageModel
        fields = ['image']
        labels = {
            'image' : 'Image'
        }
