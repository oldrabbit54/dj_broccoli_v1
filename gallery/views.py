from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, reverse
from django.db.models import Q
from django.views.generic import TemplateView, CreateView, ListView

from gallery.forms import GalleryStorageForm
from gallery.models import GalleryStorageModel
from main_menu.utils import DataMixin
from thoughts.utils import AddingMixin


# Create your views here.
class GalleryMenuView(DataMixin, TemplateView):
    template_name = 'gallery/gallery_menu.html'
    def get(self, request, *args, **kwargs):
        return HttpResponse("<h1>Sorry, the app is under construction at the moment!</h1>")
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        add_context = super().get_user_context(**kwargs)
        return context | add_context




class GalleryImageUpload(AddingMixin, DataMixin, CreateView):
    model = GalleryStorageModel
    form_class = GalleryStorageForm
    template_name = 'gallery/gallery_uploading.html'
    success_url = '/success'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        add_context = super().get_user_context(**kwargs)
        return context | add_context

    def form_valid(self, form):
        super().form_valid(form)
        super().add_author_and_time(form)
        self.object.title = form.cleaned_data['image'].name
        return super().form_valid(form)
    def get(self, request, *args, **kwargs):
        if (not self.request.user.is_authenticated):
            return HttpResponseRedirect(reverse('register'))
        return super().get(request, *args, **kwargs)
class GalleryAllImagesDisplay(DataMixin, ListView):
    paginate_by = 3
    model = GalleryStorageModel
    context_object_name = 'images'
    template_name = 'gallery/gallery_collection.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        add_context = super().get_user_context(**kwargs)
        return context | add_context

    def get_queryset(self):
        queryset = super().get_queryset()
        new_qs = queryset.filter(Q(title__endswith='.jpeg') | Q(title__endswith='.jpg') | Q(title__endswith='.png'))
        return new_qs
