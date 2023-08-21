from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.GalleryMenuView.as_view(), name='gallery'),
    # path('add_image', views.GalleryImageUpload.as_view(), name='gallery-image-add'),
    # path('image_collection', views.GalleryAllImagesDisplay.as_view(), name='gallery-image-collection'),


]
