from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
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

## Расположил данную функцию здесь, так как это представление является основным для страницы, на которую происходит редирект из формы регистрации
## И с адреса localhost:8000
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_not_author'] = not self.request.user.groups.filter(name='authors').exists()
        return context

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


class PostCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = ('news.add_post',
                           'news.change_post')
    template_name = 'add.html'
    form_class = PostForm


class PostUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = ('news.change_post',)
    template_name = 'edit.html'
    form_class = PostForm

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)


class PostDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    permission_required = ('news.delete_post',)
    template_name = 'delete.html'
    queryset = Post.objects.all()
    success_url = '/news/'
