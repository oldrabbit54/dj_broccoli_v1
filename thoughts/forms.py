from django import forms
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator

from my_profile.models import ProfileModel
from .models import NoteModel

class NoteForm(forms.ModelForm):
    class Meta:
        model = NoteModel
        fields = ['header', 'note']
        error_messages = {
            'note' : {
                'max_length' : 'Shorten up your story!',
                'required' : 'Write something!'
            },
            'header' : {
                'max_length' : 'Try to be more concise',
                'required' : 'There must be some topic..',
            }

        }
        labels = {
            'note' : 'Your text',
            'header' : 'Topic'
        }
        widgets = {
            'note' : forms.Textarea(attrs={'placeholder' : 'Spare a note..'}),
            'header' : forms.TextInput(attrs={'placeholder' : 'Topic..'})
        }