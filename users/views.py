from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic.detail import DetailView
from django.views.generic import ListView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.exceptions import ObjectDoesNotExist

from .forms import RegisterForm
from .models import BlogUser

def register(request):
    if request.method == 'POST':
        reg_form = RegisterForm(request.POST)
        if reg_form.is_valid():
            info = reg_form.cleaned_data
            username = info.get('username')
            email = info.get('email')
            passwd1 = info.get('password1')
            passwd2 = info.get('password2')
            messages.success(request, f"Usuario {username} creado con éxito.")
            # data = {
            #     'username': username,
            #     'email': email,
            #     'password1': passwd1,
            #     'password2': passwd2,
            # }
            # complete_form = RegisterForm(data)
            # if complete_form.is_valid():
            #     complete_form.save()
            #     return redirect('Reg-Success')
            return redirect('Reg-Success')
    else:
        reg_form = RegisterForm()

    register_context = {
        'form': reg_form,
    }
    return render(request, 'users/register.html', register_context)

class RegisterSuccess(TemplateView):

    template_name = 'users/reg_success.html'

# class UserList(ListView):

#     model = BlogUser
#     template_name = 'users/user_list.html'

# class UserDetail(DetailView):

#     model = BlogUser
#     template_name = 'users/details.html'
