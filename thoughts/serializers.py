from rest_framework import serializers

from my_profile.models import ProfileModel
from thoughts.models import CommentModel, NoteModel


class CommentSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        validated_data.update({'author' : self.context['request'].user.my_profile})
        return super().create(validated_data)
    class Meta:
        model = CommentModel
        fields = ['text', 'note', 'author', 'time_create']
        read_only_fields = ['author', 'time_create']

class NoteSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        validated_data.update({'author' : self.context['request'].user.my_profile})
        return super().create(validated_data)
    class Meta:
        model = NoteModel
        fields = ['header', 'note', 'author']
        read_only_fields = ['author']

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileModel
        fields = ['avatar', 'first_name', 'last_name']
