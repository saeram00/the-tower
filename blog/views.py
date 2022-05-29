from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin

from .forms import PostForm
from .models import Post


class BlogIndex(ListView):

    model = Post
    template_name = 'blog/blog-index.html'
    ordering = ('-date_posted',)
    extra_context = {
        'title': "Inicio",
    }

class PostList(ListView):

    model = Post
    template_name = 'blog/blog-list.html'
    ordering = ('-date_posted',)
    extra_context = {
        'title': "Listado de posts",
    }

class UserPostList(ListView):

    model = Post
    template_name = 'blog/user-post_list.html'
    ordering = ('-date_posted',)
    extra_context = {
        'title': "Tus Posts",
    }

def search_posts(request):
    if request.GET.get('titulo'):
        found_title = request.GET.get('titulo')
        filtered_posts = Post.objects.filter(title__icontains=found_title)
        return render(
            request,
            'blog/filter-post_list.html',
            {'title': "Resultados", 'results': filtered_posts}
        )
        
    search_context = {
        'title': "Buscar posts",
    }
    return render(request, 'blog/search-author.html', search_context)

class PostDetail(DetailView):

    model = Post
    template_name = 'blog/post_detail.html'
    extra_context = {
        'title': "Post",
    }

class PostCreate(UserPassesTestMixin, SuccessMessageMixin, CreateView):

    model = Post
    template_name = 'blog/post_create.html'
    fields = [
        'title',
        'topic',
        'content'
    ]
    success_message = "Post publicado con éxito."
    extra_context = {
        'title': "Crear Post",
    }

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        return self.request.user.is_authenticated and (
            self.request.user.is_staff
            or self.request.user.id == self.request.user.profile.id
        )

class PostUpdate(UserPassesTestMixin, SuccessMessageMixin, UpdateView):

    model = Post
    template_name = "blog/post_update.html"
    fields = [
        'title',
        'topic',
        'content'
    ]
    success_message = "Post editado con éxito."
    extra_context = {
        'title': "Editar Post",
    }

    def test_func(self):
        return self.request.user.is_authenticated and (
            self.request.user.is_staff
            or self.request.user.id == self.request.user.profile.id
        )

class PostDelete(UserPassesTestMixin, SuccessMessageMixin, DeleteView):

    model = Post
    template_name = "blog/post_delete.html"
    success_url = '/entradas/'
    success_message = "Post eliminado con éxito."
    extra_context = {
        'title': "Borrar Post",
    }

    def test_func(self):
        return self.request.user.is_authenticated and (
            self.request.user.is_staff
            or self.request.user.id == self.request.user.profile.id
        )

