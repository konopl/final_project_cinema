from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import Session, Ticket, CinemaHall
from .forms import SessionForm, CinemaHallForm

# Create your views here.


# def poster(request):
#     return render(request, 'cinema_box_office/index.html')


class Poster(ListView):
    model = Session
    template_name = 'cinema_box_office/index.html'
    context_object_name = 'session'


class CreateSession(CreateView):
    model = Session
    template_name = 'cinema_box_office/create_session.html'
    form_class = SessionForm
    http_method_names = ['post', 'get']
    success_url = '/'


class BuyTicket(CreateView):
    model = Ticket
    http_method_names = ['post', 'get']
    success_url = '/'


class CreateCinemaHall(CreateView):
    model = CinemaHall
    template_name = 'cinema_box_office/create_cinema_hall.html'
    form_class = CinemaHallForm
    success_url = '/'
