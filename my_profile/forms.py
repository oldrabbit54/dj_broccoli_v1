from django import forms
from my_profile.models import ProfileModel


class ProfileForm(forms.ModelForm):
    class Meta:
        model = ProfileModel
        fields = ['avatar', 'first_name', 'last_name', 'bio']
        widgets = {
            'avatar' : forms.FileInput(),
            'first_name' : forms.TextInput(),
            'last_name' : forms.TextInput(),
            'bio' : forms.Textarea()
        }
        labels = {
            'avatar' : 'Profile avatar',
            'first_name' : 'Name',
            'last_name' : 'Surname',
            'bio' : 'Biography',
        }
        error_messages = {
            'first_name' : {
                'max_length' : 'Too many characters(maximum 20)',
                'required' : 'Name is required',
            },
            'last_name' : {
                'max_length' : 'Too many characters(maximum 20)',
            },

        }
