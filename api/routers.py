from rest_framework.routers import DefaultRouter

from api.views import EventViewSet

events_router = DefaultRouter()
events_router.register('events', EventViewSet, basename='event')