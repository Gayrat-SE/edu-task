from .serializers import StudentCreateSerializer, StudentGroupCreateSerializer
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from user.models import Student, StudentGroup
from rest_framework.response import Response

class StudentCreate(APIView):
    
    def post(self, request):
        serializer = StudentCreateSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()

            return Response(serializer.data)

class StudentGroupCreate(CreateAPIView):
    queryset = StudentGroup.objects.all()
    serializer_class = StudentGroupCreateSerializer