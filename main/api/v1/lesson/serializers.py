from lesson.models import Event
from user.models import StudentGroup
from rest_framework import serializers
import os
class CreateEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('title', 'start_date', 'end_date',  'groups')


class GetEventsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('title', 'start_date', 'end_date', 'groups')
