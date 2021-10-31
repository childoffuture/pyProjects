from django.urls import path
from .views import NewsList, Post

urlpatterns = [
    path('', NewsList.as_view()),
    path('<int:pk>', Post.as_view()),
]