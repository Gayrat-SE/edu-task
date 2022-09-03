from rest_framework.generics import ListAPIView
from .serializers import ArchiveSerializers
from log_report.models import Log
from rest_framework.response import Response


class Archive(ListAPIView):
    queryset = Log
    serializer_class = ArchiveSerializers

    def get_queryset(self):
        archive = Log.objects.filter(username = self.request.user).exclude(method="GET").order_by('-id')
        return archive

