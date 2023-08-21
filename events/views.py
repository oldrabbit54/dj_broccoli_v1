import datetime

from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import View
from django.views.generic import CreateView, ListView, UpdateView, FormView, TemplateView
from .forms import EventForm
from .models import EventModel


from main_menu.utils import DataMixin


class EventView(DataMixin, TemplateView):
    template_name = 'events/event_main_page.html'
    def get(self, request, *args, **kwargs):
        if (not self.request.user.is_authenticated):
            return HttpResponseRedirect(reverse('register'))


        return super().get(request, *args, **kwargs)



    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        add_context = super().get_user_context(**kwargs)
        if self.request.GET:
            events = EventModel.objects.filter(expire_time=self.request.GET['date'], user=self.request.user)
            context['events_number'] = len(events)
            context['filters'] = ['By Category', 'By Recency', 'Expired']
            sort_args = []
            for fltr in self.request.GET.getlist('filter'):
                sort_arg = ''
                match fltr:
                    case 'cat_fwd' | 'cat_rev':
                        sort_arg = 'cat__id'
                        sort_arg = '-' * (bool('rev' in fltr)) + sort_arg
                        sort_args.append(sort_arg)
                    case 'add_rec_fwd' | 'add_rec_rev':
                        sort_arg = 'time_create'
                        sort_arg = '-' * (bool('rev' in fltr)) + sort_arg
                        sort_args.append(sort_arg)

                    case 'soon_fwd' | 'soon_rev':
                        sort_arg1 = 'expire_time'
                        sort_arg2 = 'expire_time_hours'
                        sort_arg1 = '-' * (bool('rev' in fltr)) + sort_arg1
                        sort_arg2 = '-' * (bool('rev' in fltr)) + sort_arg2
                        sort_args.append(sort_arg1)
                        sort_args.append(sort_arg2)

            events = events.order_by(*sort_args)
            context['events'] = events
        return context | add_context

'''
ok, some explanation
since I could not find calendar with decent date AND time pickers I divided them.
thus they are stored separately but the sorting by expire_time is done inseparably.
'''
class EventCreateView(DataMixin, CreateView):
    model = EventModel
    form_class = EventForm
    template_name = 'events/event_create.html'
    success_url = '/success'
    def get(self, request, *args, **kwargs):
        if (not self.request.user.is_authenticated):
            return HttpResponseRedirect(reverse('register'))
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        add_context = super().get_user_context(**kwargs)
        return context | add_context
    def form_valid(self, form):

        obj = form.save(commit=False)
        #obj.expire_time = datetime.datetime.combine(obj.expire_time, obj.expire_time_hours)
        #obj.expire_time_hours = None
        obj.user = self.request.user
        obj.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)






