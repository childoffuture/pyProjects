from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import *
from .models import *


class PerevalView(APIView):

    def get(self, request):
        queryset = Pereval.objects.all()
        serializer = PerevalSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PerevalSerializer(data=request.data)
        if serializer.is_valid():
            pereval = serializer.save()
            return Response(f'pereval added. New id {pereval.pk}', status=200)
        else:
            return Response(serializer.errors, status=400)
