from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Post
from django.views.generic import ListView, TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


class BlogIndex(TemplateView):

    template_name = 'blog/blog-index.html'

class PostList(ListView):

    model = Post
    template_name = 'blog/blog-list.html'

class PostDetail(DetailView):

    model = Post
    template_name = 'blog/blog-detail.html'

class PostCreate(CreateView):

    model = Post
    template_name = 'blog/post_create.html'
    success_url = 'blog/blog-list.html'
    fields = ['title', 'topic', 'content']

class PostUpdate(UpdateView):

    model = Post
    template_name = "blog/post_edit.html"
    success_url = 'blog/blog-list.html'
    fields = ['title', 'topic', 'content']

class PostDelete(DeleteView):

    model = Post
    template_name = "blog/post_delete.html"
    success_url = 'blog/blog-list.html'

