from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import *
from .models import *


class PerevalView(APIView):

#    def get(self, request):
#        queryset = Pereval.objects.all()
#        serializer = PerevalSerializer(queryset, many=True)
#        #print("get", json.dumps(serializer))
#        return Response(serializer.data)

    def post(self, request):
        result = PerevalSerializer(data=request.data)
        if result.is_valid():
            result.save()
            return Response(status=201)
        else:
            return Response(status=503)