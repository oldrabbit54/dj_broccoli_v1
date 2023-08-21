from django import forms
from .models import EventModel


class EventForm(forms.ModelForm):
    class Meta:
        model = EventModel
        fields = ['title', 'body', 'cat', 'expire_time', 'expire_time_hours']
        labels = {
            'title' : 'Title',
            'body' : 'Content',
            'cat' : 'Category',
            'expire_time' : 'Till',
            'expire_time_hours' : 'Time',
        }

        widgets = {
            'title': forms.Textarea(attrs={'placeholder': 'Spare a note..'}),
            'body': forms.TextInput(attrs={'placeholder': 'Topic..'}),
            'expire_time_hours' : forms.TimeInput()
        }
