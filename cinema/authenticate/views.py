# from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView
# from authenticate.forms import RegisterForm
from authenticate.models import User
from authenticate.forms import UserForm


# Create your views here.


class Login(LoginView):
    template_name = 'authenticate/login.html'
    redirect_authenticated_user = True


class Logout(LogoutView):
    template_name = 'authenticate/logout.html'


class Register(CreateView):
    model = User
    template_name = 'authenticate/register.html'
    form_class = UserForm
    success_url = '/authenticate/login/'
