from django.urls import path
from .views import Poster

urlpatterns = [
    path('', Poster.as_view(), name='poster'),
]