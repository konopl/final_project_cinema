from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView
# from authenticate.forms import RegisterForm
# from authenticate.models import User


# Create your views here.


class Login(LoginView):
    pass


class Logout(LogoutView):
    pass


class Register(CreateView):
    pass
