from django.urls import path, include
from .views import *

urlpatterns = [
    path('', EventView.as_view(), name='event-page'),
    path('create_event', EventCreateView.as_view(), name='event-create')
]