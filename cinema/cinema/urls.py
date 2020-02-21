"""cinema URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from cinema_box_office.views import SessionViewSet
from authenticate.views import UserViewSet


router = routers.DefaultRouter()
router.register(r'session', SessionViewSet)
router.register(r'auth', UserViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('authenticate/', include('authenticate.urls')),
    path('', include('cinema_box_office.urls')),
    path('', include(router.urls)),

]
