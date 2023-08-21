from django.db.models import Q, QuerySet
from rest_framework import viewsets, generics, mixins
from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.urls import reverse
from django.views.generic import TemplateView, CreateView, UpdateView, ListView
from django.contrib.auth.models import User
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from main_menu.utils import DataMixin
from my_profile.models import ProfileModel
from .forms import NoteForm, NoteModel
import urllib.parse

from .models import CommentModel
from .permissions import IsOwnerOrReadOnly
from .serializers import NoteSerializer, CommentSerializer, ProfileSerializer


# Create your views here.
class ThoughtsMenuView(DataMixin, TemplateView):
    template_name = 'thoughts/thoughts_menu.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        add_context = super().get_user_context(**kwargs)
        return context | add_context

class NoteCreateView(DataMixin, CreateView):
    template_name = 'thoughts/create_note.html'
    form_class = NoteForm
    model = NoteModel
    success_url = '/thoughts/posts'
    def get(self, request, *args, **kwargs):
        if(not self.request.user.is_authenticated):
            return HttpResponseRedirect(reverse('register'))
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        add_context = super().get_user_context(**kwargs)
        return context | add_context

    def form_valid(self, form):
        profile_obj = User.objects.get(id=self.request.user.id).my_profile
        new_note_obj = form.save()
        new_note_obj.author = profile_obj
        return super().form_valid(form)

class NoteUpdateView(DataMixin, UpdateView):
    template_name = 'thoughts/create_note.html'
    form_class = NoteForm
    model = NoteModel
    success_url = '/thoughts/posts'
    def get(self, request, *args, **kwargs):
        if (not self.request.user.is_authenticated):
            return HttpResponseRedirect(reverse('register'))
        note = NoteModel.objects.get(id=kwargs['pk'])
        if(note.author.id != self.request.user.my_profile.id):
            return HttpResponseNotFound('Note does not exist')
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        add_context = super().get_user_context(**kwargs)
        return context | add_context



class PostsView(DataMixin, ListView):
    template_name = 'thoughts/posts.html'
    model = NoteModel
    context_object_name = 'posts'
    sort_modes = ['name_sort', 'date_sort']

    def get(self, request, *args, **kwargs):
        if(not self.request.user.is_authenticated):
            return HttpResponseRedirect(reverse('register'))
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        qs = self.model.objects.none()
        get_request = self.request.GET

        def sorting(mode, *args):
            order_fields = ['-' * (mode == 'reverse') + i for i in args]
            return self.model.objects.all().order_by(*order_fields)
        if get_request.get('name_sort', None):
            qs = qs | sorting(get_request.get('name_sort'), 'author__first_name', 'author__last_name')
        elif get_request.get('date_sort', None):
            qs = qs | sorting(get_request.get('date_sort'), 'time_create')
        else:
            qs = self.model.objects.all()
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        add_context = super().get_user_context(**kwargs)
        sorts = {'name_sort' : {'name_sort':'forward' if 'name_sort' not in self.request.GET else 'reverse'},
                 'date_sort' : {'date_sort' : 'forward' if 'date_sort' not in self.request.GET else 'reverse'}}
        context['name_sort'] = reverse('posts-preview') + '?' + urllib.parse.urlencode(sorts['name_sort'])
        context['date_sort'] = reverse('posts-preview') + '?' + urllib.parse.urlencode(sorts['date_sort'])
        context['add_comment_url'] = reverse('comment-list') + '?note_id='
        context['this_user'] = ProfileModel.objects.get(id=add_context['this_user_id'])
        return context | add_context


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (IsOwnerOrReadOnly, )
    queryset = CommentModel.objects.all()

class NoteViewSet(viewsets.ModelViewSet):
    serializer_class = NoteSerializer
    permission_classes = (IsOwnerOrReadOnly, )
    queryset = NoteModel.objects.all()


    @action(detail=True, methods=['get', 'post'], permission_classes=(IsOwnerOrReadOnly, ))
    def get_comments(self, request, pk=None):

        note = get_object_or_404(self.queryset, pk=pk)
        comments = note.notes.all()
        return Response({'comments' : CommentSerializer(comments, many=True).data})

class ProfileViewSet(mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     GenericViewSet):
    serializer_class = ProfileSerializer
    queryset = ProfileModel.objects.all()

