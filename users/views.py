from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic.detail import DetailView
from django.views.generic import ListView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.exceptions import ObjectDoesNotExist

from .forms import BlogUserForm
from .models import Profile


def register(request):
    if request.method == 'POST':
        bloguser_form = BlogUserForm(request.POST)
        if bloguser_form.is_valid():
            bloguser_form.save()
            info = bloguser_form.cleaned_data
            username = info.get('username')
            email = info.get('email')
            new_user = Profile(
                nombre_usuario=username,
                email=email,
                usuario=User.objects.get(username=username)
            )
            new_user.save()
            messages.success(request, f"Usuario {username} creado con éxito.")
            return redirect('Reg-Success')
        else:
            messages.warning(request, f"Datos inválidos. Por favor intente nuevamente.")

    else:
        bloguser_form = BlogUserForm()

    register_context = {
        'title': "Registro",
        'form': bloguser_form,
    }
    return render(request, 'users/register.html', register_context)


class RegisterSuccess(LoginRequiredMixin, TemplateView):

    template_name = 'users/reg_success.html'
    extra_context = {
        'title': "¡Registro Exitoso!",
    }

class UserLogin(LoginView):

    template_name = 'users/login.html'
    extra_context = {
        'title': "Login",
    }

class UserLogout(LoginRequiredMixin, LogoutView):

    template_name = 'users/logout.html'
    extra_context = {
        'title': "Logout",
    }

class UserList(LoginRequiredMixin, ListView):

    model = Profile
    template_name = 'users/user_list.html'
    extra_context = {
        'title': "Lista de usuarios",
        'blog_users': Profile.objects.all(),
    }

class UserDetail(LoginRequiredMixin, DetailView):

    model = Profile
    template_name = 'users/detail.html'
    extra_context = {
        'title': "Detalle",
    }  
