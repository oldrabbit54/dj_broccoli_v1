from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from . import views
from .routers import comments_router

urlpatterns = [
    path('create_note', views.NoteCreateView.as_view(), name='note-create'),
    path('update_note/<int:pk>', views.NoteUpdateView.as_view(), name='note-update'),
    path('posts', views.PostsView.as_view(), name='posts-preview'),
]