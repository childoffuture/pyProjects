from rest_framework.response import Response
from rest_framework.views import APIView


from .models import Category, Dish
from .serializers import CategorySerializer, DishSerializer


class CategoryListView(APIView):
    def get(self, request):
        queryset = Category.objects.all()
        serializer = CategorySerializer(queryset, many=True)
        return Response(serializer.data)


class CategoryView(APIView):
    def get(self, request, pk):
        queryset = Dish.objects.filter(id_category=pk)
        serializer = DishSerializer(queryset, many=True)
        return Response(serializer.data)


class DishView(APIView):
    def get(self, request, pk):
        queryset = Dish.objects.get(id=pk)
        serializer = DishSerializer(queryset, many=False)
        return Response(serializer.data)

