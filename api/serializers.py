from django.contrib.auth.models import User
from rest_framework import serializers

from events.models import EventModel


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventModel
        exclude = ['time_create', 'user']

    def save(self, **kwargs):
        # in case request sender puts some other id we explicitly set it
        # at the point of saving the instance
        self.validated_data['user'] = self.context['request'].user
        # Note:
        # Turns out you can populate validated_data with literally anything
        # as long as such field with given argument can be assigned to a model instance
        return super().save(**kwargs)




