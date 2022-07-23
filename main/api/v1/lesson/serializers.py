from lesson.models import Event
from user.models import StudentGroup
from rest_framework import serializers
import os
import requests
import json
from datetime import datetime

class DTEncoder(json.JSONEncoder):
    def default(self, obj):
        # 👇️ if passed in object is datetime object
        # convert it to a string
        if isinstance(obj, datetime):
            return str(obj)
        # 👇️ otherwise use the default behavior
        return json.JSONEncoder.default(self, obj)
class CreateEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('title', 'start_date', 'end_date',  'groups')

    def create(self, validated_data):
        lesson = Event.objects.create(groups = validated_data['groups'], title = validated_data['title'], start_date = validated_data['start_date'],
            end_date = validated_data['end_date'], teacher_id = self.context['request'].user.teacher.id)
        data = requests.post("https://api.zoom.us/v2/users/me/meetings", headers={
            "Authorization": f"Bearer { self.context['request'].session['zoom_access_token'] } ",
            "content-type": "application/json"
            }, data=json.dumps({
            "topic": f"Interview with { lesson.groups.name }",
            "type": 2,
            "start_time": validated_data['end_date'],
            }, default=str))

        lesson.zoom_join_url = data.json()["join_url"]
        lesson.zoom_start_url = data.json()["start_url"]

        lesson.save()
        return lesson


class GetEventsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('title', 'start_date', 'end_date', 'groups')
