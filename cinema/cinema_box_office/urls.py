from django.urls import path
from .views import (Poster, CreateSession, BuyTicket, CreateCinemaHall,
                    CreateMovie, BasketListView, UpdateSession, DeleteSession)

urlpatterns = [
    path('', Poster.as_view(), name='poster'),
    path('create_session/', CreateSession.as_view(), name='create_session'),
    path('update_session/<int:pk>', UpdateSession.as_view(), name='update_session'),
    path('delete_session/<int:pk>', DeleteSession.as_view(), name='delete_session'),
    path('create_cinema_hall/', CreateCinemaHall.as_view(), name='create_cinema_hall'),
    path('buy_ticket/', BuyTicket.as_view(), name='buy_ticket'),
    path('create_movie/', CreateMovie.as_view(), name='create_movie'),
    path('basket/', BasketListView.as_view(), name='basket'),
]
