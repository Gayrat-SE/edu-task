from rest_framework import serializers
from chat.models import Message, MessageRoom, Room



class ChatSerializersCreate(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['content', 'group', 'date_added',]

    
    def create(self, validated_data):

        message = Message.objects.create(**validated_data)

        return message

class ChatMessageSerializers(serializers.ModelSerializer):
    class Meta:
        model = MessageRoom
        fields = ['content', 'room', 'date_added', 'users']

class RoomSerializersCreate(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['name', 'group', 'owner']