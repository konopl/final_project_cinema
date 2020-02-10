from django.urls import path
from .views import Poster, CreateSession, BuyTicket

urlpatterns = [
    path('', Poster.as_view(), name='poster'),
    path('create_session/', CreateSession.as_view(), name='create_session'),
    path('buy_ticket/', BuyTicket.as_view(), name='buy_ticket'),
]
