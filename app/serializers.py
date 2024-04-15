from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Note


class NoteSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=False, allow_blank=True, max_length=100)
    text = serializers.CharField()
    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(view_name='note-highlight', format='html')

    def create(self, validated_data):
        return Note.objects.create(**validated_data)


class UserSerializer(serializers.Serializer):
    notes = serializers.HyperlinkedIdentityField(many=True, view_name='note-detail', read_only=True)
