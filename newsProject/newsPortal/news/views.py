from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .filters import PostFilter
from .forms import PostForm


class PostList(ListView):
    model = Post
    template_name = 'news.html'
    context_object_name = 'postList'
    queryset = Post.objects.order_by('-created')
    # Пагинацию вместо 10, как в задании, поставил 4, т. к. 10 новостей не помещались на весь экран,
    # ну и чтобы не плодить одинаковых записей в БД, а просто продемонстрировать работу постраничного просмотра
    paginate_by = 4


class SearchList(PostList):
    template_name = 'search.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = PostFilter(self.request.GET, queryset=self.get_queryset())
        context['form'] = PostForm()
        return context


class PostView(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'postView'


class PostCreateView(CreateView):
    template_name = 'add.html'
    form_class = PostForm


class PostUpdateView(UpdateView):
    template_name = 'edit.html'
    form_class = PostForm

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)


class PostDeleteView(DeleteView):
    template_name = 'delete.html'
    queryset = Post.objects.all()
    success_url = '/news/'
