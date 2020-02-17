from django.shortcuts import render, HttpResponse
from django.views.generic import ListView, CreateView
from .models import Session, Ticket, CinemaHall, Movie
from .forms import SessionForm, TicketForm, CinemaHallForm, CreateMovieForm
from datetime import datetime
import pytz

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

    def form_valid(self, form):
        local = pytz.timezone('Europe/Kiev')
        start_from_form = (form.data['start_at'])
        end_from_form = (form.data['end_at'])
        start_new_session = local.localize(datetime.strptime(start_from_form, '%Y-%m-%d %H:%M:%S'))
        end_new_session = local.localize(datetime.strptime(end_from_form, '%Y-%m-%d %H:%M:%S'))
        if Session.objects.all() and (Session.objects.filter(cinema_hall=form.data['cinema_hall'])):
            # import pdb
            # pdb.set_trace()
            for obj in (Session.objects.filter(cinema_hall=form.data['cinema_hall'])):
                start_from_object = local.localize(datetime.strptime(str(obj.start_at), '%Y-%m-%d %H:%M:%S'))
                end_from_object = local.localize(datetime.strptime(str(obj.end_at), '%Y-%m-%d %H:%M:%S'))
                # import pdb
                # pdb.set_trace()
                if ((start_new_session >= start_from_object) and (start_new_session <= end_from_object)) or ((end_new_session >= start_from_object) and (end_new_session <= end_from_object)):
                    return HttpResponse('  гавно собачье ')
                else:
                    self.object = form.save()
                    return super().form_valid(form)
        else:
            self.object = form.save()
            return super().form_valid(form)


class BuyTicket(CreateView):
    model = Ticket
    http_method_names = ['post', 'get']
    success_url = '/'
    form_class = TicketForm
    template_name = 'cinema_box_office/user.html'


class CreateCinemaHall(CreateView):
    model = CinemaHall
    template_name = 'cinema_box_office/create_cinema_hall.html'
    form_class = CinemaHallForm
    success_url = '/'


class CreateMovie(CreateView):
    model = Movie
    template_name = 'cinema_box_office/create_movie.html'
    form_class = CreateMovieForm
    success_url = '/'





