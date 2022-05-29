from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import ListView, TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView

from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin

from .forms import BlogUserForm, UserUpdateForm, ProfileUpdateForm
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
                usuario=User.objects.get(username=username),
                nombre_usuario=User.objects.get(username=username),
                email=User.objects.get(email=email)
            )
            new_user.save()
            messages.success(request, f"Usuario {username} creado con éxito.")
            return redirect('Reg-Success')
        else:
            messages.warning(request,
                             f"Datos inválidos. Por favor intente nuevamente.")

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

class UserList(ListView):

    model = Profile
    template_name = 'users/user_list.html'
    extra_context = {
        'title': "Lista de usuarios",
    }

class UserDetail(DetailView):

    model = Profile
    template_name = 'users/profile.html'
    extra_context = {
        'title': "Detalle",
    }  

class UserUpdate(UserPassesTestMixin, SuccessMessageMixin, UpdateView):

    model = User
    template_name = 'users/user_update.html'
    success_url = '/usuarios/listado/'
    fields = (
        'username',
        'email',
    )
    success_message = "Perfil editado con éxito."
    extra_context = {
        'title': "Editar usuario",
    }

    def test_func(self):
        return self.request.user.is_authenticated and (
            self.request.user.is_staff
            or self.request.user.id is self.kwargs['pk']
        )

class ProfilePicUpdate(UserPassesTestMixin, SuccessMessageMixin, UpdateView):

    model = Profile
    template_name = 'users/profile_pic_update.html'
    fields = (
        'foto_perfil',
    )
    success_message = "Foto de perfil editada con éxito."
    extra_context = {
        'title': "Editar foto perfil",
    }

    def test_func(self):
        return self.request.user.is_authenticated and (
            self.request.user.is_staff
            or self.request.user.id is self.kwargs['pk']
        )

class UserDelete(UserPassesTestMixin, SuccessMessageMixin, DeleteView):

    model = User
    template_name = 'users/user_delete.html'
    success_url = '/'
    success_message = "Usuario eliminado con éxito."
    extra_context = {
        'title': "Eliminar usuario",
    }

    def test_func(self):
        return self.request.user.is_authenticated and (
            self.request.user.is_staff
            or self.request.user.id is self.kwargs['pk']
        )

