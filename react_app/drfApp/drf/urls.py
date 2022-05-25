from django.urls import path
from .views import *

urlpatterns = [
    path('', CategoryListView.as_view()),
    path('category/<int:pk>', CategoryView.as_view()),
    path('dish/<int:pk>', DishView.as_view()),
]
