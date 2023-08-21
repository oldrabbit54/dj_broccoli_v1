import datetime

from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.generic import TemplateView, DetailView, ListView, CreateView, UpdateView, FormView

from main_menu.utils import DataMixin
from my_profile.forms import ProfileForm
from my_profile.models import ProfileModel


# Create your views here.
class ProfileView(DataMixin, ListView):
    model = ProfileModel
    context_object_name = 'profile_object'
    template_name = 'my_profile/my_profile_overview.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        add_context = super().get_user_context(**kwargs)
        context['user_note'] = get_object_or_404(User, id=self.request.user.id)
        context['img_url'] = context['profile_object'].avatar.url
        return context | add_context

    def get(self, request, *args, **kwargs):
        if (not self.request.user.is_authenticated):
            return HttpResponseRedirect(reverse('register'))
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        user_profile = get_object_or_404(ProfileModel, user_id=self.request.user.id)
        return user_profile


class ProfileEditView(DataMixin, CreateView):
    # так как на момент разработки(!) колво всех юзеров не совпадает с колвом всех профилей,
    # то будет ошибка, сейчас профиль будет извлекаться через related_name,
    # но в последующем колво пользователей должно(!) совпадать с колвом профилей(их id совпадать)
    model = ProfileModel
    form_class = ProfileForm
    template_name = 'my_profile/my_profile_edit.html'
    success_url = '/success'
    def get_queryset(self):
        return ProfileModel.objects.get(id=self.request.user.my_profile.id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        add_context = super().get_user_context(**kwargs)
        context['form'] = ProfileForm(instance=self.get_queryset())
        context['avatar'] = self.get_queryset().avatar
        return context | add_context

    def get(self, request, *args, **kwargs):
        if (not self.request.user.is_authenticated):
            return HttpResponseRedirect(reverse('register'))
        return super().get(request, *args, **kwargs)

    def form_valid(self, form):
        profile_object = self.get_queryset()
        changed_data_dict = {key: value for key, value in form.cleaned_data.items() if key in form.changed_data}
        changed_data_dict['avatar'] = form.save(commit=False).avatar
        avatar = changed_data_dict['avatar']
        avatar.save(avatar.name, avatar)
        ProfileModel.objects.filter(id=profile_object.id).update(**changed_data_dict)
        if_changed = True
        context = {'form': form, 'if_changed': if_changed} | super().get_user_context()
        context['avatar'] = self.get_queryset().avatar
        return render(self.request, 'my_profile/my_profile_edit.html',
                      context=context)


