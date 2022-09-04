from rest_framework.generics import ListAPIView
from .serializers import ArchiveSerializers
from log_report.models import Log
from rest_framework_datatables import pagination as dt_pagination

class Archive(ListAPIView):
    queryset = Log.objects.all()
    serializer_class = ArchiveSerializers

    pagination_class = dt_pagination.DatatablesLimitOffsetPagination

    def get_queryset(self):
        archive = Log.objects.filter(username = self.request.user).exclude(method="GET").order_by('-id')
        return archive

