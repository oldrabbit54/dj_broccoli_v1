from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Invisible, ReCaptchaV3
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms


from main_menu.models import HelpModel
# class RegisterConfirmationForm(forms.ModelForm):
#     code = forms.IntegerField(label='Enter the code', errors = {'Wrong code, try again'})

class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Enter desired username', widget=forms.TextInput())
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput())
    password2 = forms.CharField(label='Password again', widget=forms.PasswordInput())
    email = forms.EmailField(label='Your email address', widget=forms.EmailInput())
    captcha = ReCaptchaField()


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Your username')
    password = forms.CharField(label='Password', widget=forms.PasswordInput())


class HelpForm(forms.ModelForm):
    class Meta:
        model = HelpModel
        fields = ['note']
        labels = {
            'note' : 'Question',
        }

