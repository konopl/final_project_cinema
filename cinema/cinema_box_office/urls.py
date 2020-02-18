from django.urls import path
from .views import Poster, CreateSession, BuyTicket, CreateCinemaHall, CreateMovie, BasketListView

urlpatterns = [
    path('', Poster.as_view(), name='poster'),
    path('create_session/', CreateSession.as_view(), name='create_session'),
    path('create_cinema_hall/', CreateCinemaHall.as_view(), name='create_cinema_hall'),
    path('buy_ticket/', BuyTicket.as_view(), name='buy_ticket'),
    path('create_movie/', CreateMovie.as_view(), name='create_movie'),
    path('basket/', BasketListView.as_view(), name='basket'),
]
