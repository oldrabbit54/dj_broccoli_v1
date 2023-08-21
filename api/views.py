from django.shortcuts import render
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from .permissions import TestPermission
from .serializers import EventSerializer

from events.models import EventModel


# Create your views here.

class EventViewSet(ModelViewSet):
    serializer_class = EventSerializer
    permission_classes = (IsAuthenticated,)
    #permission_classes = (TestPermission, )

    def get_queryset(self):
        # user is not supposed to work with other people's events
        return EventModel.objects.filter(user=self.request.user.id)




