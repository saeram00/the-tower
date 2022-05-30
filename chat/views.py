from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin

from .models import Message


class MessageList(UserPassesTestMixin, ListView):

    model = Message
    template_name = 'chat/inbox.html'
    ordering = ('-fecha_emision',)
    extra_context = {
        'title': "Bandeja de entrada",
    }

    def test_func(self):
        return self.request.user.is_authenticated and (
            self.request.user.is_staff
            or self.request.user.id == self.request.user.profile.id
        )

def search_messages(request):
    if request.GET.get('asunto'):
        found_message = request.GET.get('asunto')
        results = Message.objects.filter(asunto__icontains=found_message)
        return render(
            request,
            'chat/search_results.html',
            {'title': "Resultados", 'results': results}
        )
        
    search_context = {
        'title': "Buscar mensajes",
    }
    return render(request, 'chat/search_messages.html', search_context)

class MessageDetail(UserPassesTestMixin, DetailView):

    model = Message
    template_name = 'chat/message_detail.html'
    extra_context = {
        'title': "Mensaje",
    }

    def test_func(self):
        return self.request.user.is_authenticated and (
            self.request.user.is_staff
            or self.request.user.id == self.request.user.profile.id
        )

class MessageCreate(UserPassesTestMixin, SuccessMessageMixin, CreateView):

    model = Message
    template_name = 'chat/message_create.html'
    fields = (
        'destinatario',
        'asunto',
        'contenido'
    )
    success_url = '/chat/inbox/'
    success_message = "Mensaje enviado con éxito."
    extra_context = {
        'title': "Escribir mensaje",
    }

    def form_valid(self, form):
        form.instance.remitente = self.request.user
        return super().form_valid(form)

    def test_func(self):
        return self.request.user.is_authenticated and (
            self.request.user.is_staff
            or self.request.user.id == self.request.user.profile.id
        )

class MessageUpdate(UserPassesTestMixin, SuccessMessageMixin, UpdateView):

    model = Message
    template_name = "chat/message_update.html"
    fields = (
        'asunto',
        'contenido'
    )
    success_message = "Mensaje editado con éxito."
    extra_context = {
        'title': "Editar mensaje",
    }

    def test_func(self):
        return self.request.user.is_authenticated and (
            self.request.user.is_staff
            or self.request.user.id == self.request.user.profile.id
        )

class MessageDelete(UserPassesTestMixin, SuccessMessageMixin, DeleteView):

    model = Message
    template_name = "chat/message_delete.html"
    success_url = '/chat/inbox/'
    success_message = "Mensaje eliminado con éxito."
    extra_context = {
        'title': "Borrar mensaje",
    }

    def test_func(self):
        return self.request.user.is_authenticated and (
            self.request.user.is_staff
            or self.request.user.id == self.request.user.profile.id
        )

