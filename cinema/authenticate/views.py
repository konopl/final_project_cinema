from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView
from authenticate.models import User
from authenticate.forms import UserForm
from authenticate.api.serializer import UserSerializer
from rest_framework import routers, serializers, viewsets, permissions


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


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
