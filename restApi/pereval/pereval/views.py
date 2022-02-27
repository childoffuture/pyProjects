from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import *
from .models import *


class PerevalView(APIView):

    def get(self, request):
        queryset = PerevalAdded.objects.all()
        serializer = PerevalSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        result = PerevalSerializer(data=request.data)
        #print(result)
        if result.is_valid():
            result.save()
            return Response(status=201)
        else:
            return Response(status=503)

