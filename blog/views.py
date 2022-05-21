from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Post
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


class PostList(ListView):

    model = Post
    post_template = 'blog/blog-index.html'

class PostDetail(DetailView):

    model = Post
    detail_template = 'blog/blog-detail.html'

class PostCreate(CreateView):

    model = Post
    success_url = 'blog/blog-list.html'
    fields = ['title', 'topic', 'content']

class PostUpdate(UpdateView):

    model = Post
    success_url = 'blog/blog-list.html'
    fields = ['title', 'topic', 'date_posted']

class PostDelete(DeleteView):

    model = Post
    success_url = 'blog/blog-list.html'

