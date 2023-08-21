from django.http import HttpRequest
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView

from main_menu.utils import DataMixin


class success_msg(DataMixin, TemplateView):
    template_name = 'success.html'

