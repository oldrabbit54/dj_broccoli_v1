import secrets
import requests
import urllib.parse
from django.contrib.auth import logout, login
from django.contrib.auth.models import User
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.contrib.auth.views import LoginView
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail, EmailMultiAlternatives
from django.shortcuts import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.safestring import mark_safe
from django.views.generic import CreateView, View, TemplateView, FormView

from .forms import RegisterUserForm, LoginUserForm, HelpForm
from .models import HelpModel, SessionToken
from .utils import DataMixin
from my_profile.models import ProfileModel

account_activation_token = PasswordResetTokenGenerator()
categories = [
    {'name': mark_safe('Gallery'), 'url': mark_safe('gallery'),
     'description': 'Your favorite(and not only:D) photos all here!'},
    {'name': 'Thoughts', 'url': 'thoughts', 'description':
        '''Post some of your deepest secrets anonymously.
        Do not be afraid, any problem could be solved if you are brave enough!
        '''
     },
    {'name': 'Profile', 'url': 'my_profile', 'description': 'Tell us about yourself!'}
    # {'name' : 'thots', 'url' : 'thots'},
    # {'name' : 'help', 'url' : 'help'}

]
client_id = 'INSERT YOURS'
app_key = 'INSERT YOURS'


def VK_through_auth(request):
    if request.GET.get('code', None):
        params = {
            'client_id': client_id,
            'client_secret': app_key,
            'redirect_uri': 'http://127.0.0.1:1970/vk_thru_auth',
            'code': request.GET.get('code', None),
            'v': '5.131'
        }
        auth_response = 'https://oauth.vk.com/access_token?' + urllib.parse.urlencode(params)
        response = requests.get(auth_response)
        resp = response.json()
        if resp.get('access_token', None):
            vk_user = SessionToken.objects.filter(vk_user_id=resp.get('user_id'))
            if vk_user:
                vk_user.update(vk_auth_token=resp.get('access_token'))
                login(request, vk_user[0].user)
            else:
                new_user = User.objects.create(
                    username=resp.get('email'),
                    email=resp.get('email'),
                    password='nfweWgnenjb',
                )
                SessionToken.objects.create(
                    vk_auth_token=resp.get('access_token'),
                    vk_user_id=resp.get('user_id'),
                    user=new_user,
                )
                profile = ProfileModel(
                    first_name=new_user.username, last_name=new_user.last_name,
                    user=new_user, avatar='avatars/Screenshot_5.png')
                profile.save()
                login(request, new_user)
            return HttpResponseRedirect('/')
        else:
            return HttpResponse('Something went wrong..')


class HomePageView(DataMixin, TemplateView):
    template_name = 'main_menu/home_page.html'

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['main_categories'] = categories
        add_context = super().get_user_context(**kwargs)
        return context | add_context


def VKAuth(request):
    params = {
            'client_id': client_id,
            'redirect_uri': 'http://127.0.0.1:1970/vk_thru_auth',
            'display': 'page',
            'scope': 'email,offline',
            'response_type': 'code',
        }
    auth_response = 'https://oauth.vk.com/authorize?' + urllib.parse.urlencode(params)
    return HttpResponseRedirect(auth_response)

class RegisterUserView(DataMixin, CreateView):
    model = User
    form_class = RegisterUserForm
    success_url = '/success'
    template_name = 'main_menu/register.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['main_categories'] = categories
        add_context = super().get_user_context(**kwargs)
        return context | add_context

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_active = False
        user.email = form.cleaned_data['email']
        user.save()
        current_site = get_current_site(self.request)
        token = account_activation_token.make_token(user)
        message = render_to_string('main_menu/letter_generation.html', context={
            'uid': urlsafe_base64_encode(force_bytes(user.id)),
            'user': user,
            'domain': current_site.domain,
            'token': token,
        })

        to_email = form.cleaned_data['email']
        email = EmailMultiAlternatives(subject='Email confirmation', body='Confirmation is here!',
                                       from_email='capy@buro.net',
                                       to=[to_email])
        email.attach_alternative(message, "text/html")
        email.send()
        return HttpResponse('Waiting for your confirmation honey')

def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        # return redirect('home')
        profile = ProfileModel(
            first_name=user.username, last_name=user.last_name, user=user, avatar='avatars/Screenshot_5.png')
        profile.save()
        return HttpResponseRedirect('/')
    else:
        user.delete()
        return HttpResponse('Activation link is invalid!')


class LoginUserView(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'main_menu/login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        add_context = super().get_user_context(**kwargs)
        return context | add_context

    def get_success_url(self):
        return reverse('home-page')


class HelpPageView(DataMixin, CreateView):
    template_name = 'main_menu/help_page.html'
    model = HelpModel
    form_class = HelpForm
    success_url = '/success'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        add_context = super().get_user_context(**kwargs)
        return context | add_context

    def get(self, request, *args, **kwargs):
        if (not self.request.user.is_authenticated):
            return HttpResponseRedirect(reverse('register'))
        return super().get(request, *args, **kwargs)


    def form_valid(self, form):
        profile_obj = User.objects.get(id=self.request.user.id).my_profile
        new_note_obj = form.save()
        new_note_obj.author = profile_obj
        return super().form_valid(form)


class EmailSendView(View):
    def get(self, request, *args, **kwargs):
        code = secrets.randbelow(1000000) + 100000
        html_message = render_to_string('main_menu/letter_generation.html', context={'code': code})
        send_mail('Goodbye, Django user', 'You must be awaiting', 'lol@kek.ru', ['sharpiron@mail.ru'],
                  html_message=html_message
                  )
        return HttpResponseRedirect('/success')


def log_user_out(request):
    logout(request)
    return HttpResponseRedirect(reverse('home-page'))
