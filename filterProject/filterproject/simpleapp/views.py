from django.views.generic import ListView, DetailView
from .models import News
import datetime

class NewsList(ListView):
    model = News
    template_name = 'news.html'
    context_object_name = 'news'
    queryset = News.objects.order_by('-created')

class Post(DetailView):
    model = News
    template_name = 'post.html'
    context_object_name = 'post'

