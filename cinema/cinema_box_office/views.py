from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import Session, Ticket
from .forms import SessionForm

# Create your views here.


# def poster(request):
#     return render(request, 'cinema_box_office/index.html')


class Poster(ListView):
    model = Session
    template_name = 'cinema_box_office/index.html'
    context_object_name = 'session'


class CreateSession(CreateView):
    model = Session
    template_name = 'cinema_box_office/index.html'
    form_class = SessionForm
    http_method_names = ['post', 'get']
    success_url = '/'


class BuyTicket(CreateView):
    model = Ticket
    http_method_names = ['post', 'get']
    success_url = '/'


class CreateCinemaHall(CreateView):
    pass
