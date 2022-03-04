from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import *
from .models import *


class PerevalRecordView(APIView):

    def get(self, request, pk):
        if Pereval.objects.filter(id=pk).exists():
            pereval = Pereval.objects.get(id=pk)
            return Response(self.prepare_result(pereval))
        else:
            return Response('Record not found', status=503)

    def put(self, request, pk):
        if Pereval.objects.filter(id=pk).exists():
            pereval = Pereval.objects.get(id=pk)
            serializer = PerevalSerializer(pereval, data=request.data)
            if serializer.is_valid():
                pereval = serializer.save()
                return Response(f'pereval updated. Id {pereval.pk}', status=200)
            else:
                return Response(serializer.errors, status=400)
        else:
            return Response('Record not found', status=503)

    def prepare_result(self, pereval):
        serializer = PerevalSerializer(pereval, many=False)
        return serializer.data


class PerevalStatusView(PerevalRecordView):

    def prepare_result(self, pereval):
        return f'status: {pereval.status}'


class PerevalView(APIView):

    def get(self, request):
        # username = 'vpupkin' # for test
        username = request.user.username
        queryset = Pereval.objects.filter(raw_data__user__contains={'id': username})
        serializer = PerevalSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PerevalSerializer(data=request.data)
        if serializer.is_valid():
            pereval = serializer.save()
            return Response(f'pereval added. New id {pereval.pk}', status=200)
        else:
            return Response(serializer.errors, status=400)
