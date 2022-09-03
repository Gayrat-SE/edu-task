from rest_framework import serializers
from log_report.models import Log
from api.v1.user.serializers import UserListSerializers

class ArchiveSerializers(serializers.ModelSerializer):
    username = serializers.SerializerMethodField(read_only = True)
    class Meta:
        model = Log
        fields = '__all__'
    
    def get_username(self, obj):
        id = obj.username

        serializer_user = UserListSerializers(id, many=False)

        return serializer_user.data
