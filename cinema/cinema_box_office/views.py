from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Session, Ticket, CinemaHall, Movie
from .forms import SessionForm, TicketForm, CinemaHallForm, CreateMovieForm
from datetime import datetime
import pytz
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from rest_framework import routers, serializers, viewsets, permissions
from cinema_box_office.api.serializer import SessionSerializer
from django.urls import reverse_lazy
from rest_framework.permissions import IsAuthenticatedOrReadOnly

# Create your views here.


class Poster(ListView):
    model = Session
    template_name = 'cinema_box_office/index.html'
    # form_class = SessionForm
    http_method_names = ['get']
    # queryset = Session.objects.all()
    context_object_name = 'session_list'

    def get(self, request, *args, **kwargs):
        self.object_list = self.get_queryset()
        allow_empty = self.get_allow_empty()
        if not allow_empty:
            # When pagination is enabled and object_list is a queryset,
            # it's better to do a cheap query than to load the unpaginated
            # queryset in memory.
            if self.get_paginate_by(self.object_list) is not None and hasattr(self.object_list, 'exists'):
                is_empty = not self.object_list.exists()
            else:
                is_empty = not self.object_list
            if is_empty:
                raise Http404(_('Empty list and “%(class_name)s.allow_empty” is False.') % {
                    'class_name': self.__class__.__name__,
                })
        context = self.get_context_data()
        return self.render_to_response(context)


class SessionViewSet(viewsets.ModelViewSet):
    queryset = Session.objects.all()
    serializer_class = SessionSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class CreateSession(CreateView, LoginRequiredMixin):
    model = Session
    template_name = 'cinema_box_office/create_session.html'
    form_class = SessionForm
    http_method_names = ['post', 'get']
    success_url = '/'

    login_url = '/authenticate/login/'

    def dispatch(self, request, *args, **kwargs):
        if (not request.user.is_authenticated) or ( not request.user.is_superuser):
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)

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
                import pdb
                pdb.set_trace()
                if ((start_new_session >= start_from_object) and (start_new_session <= end_from_object)) or ((end_new_session >= start_from_object) and (end_new_session <= end_from_object)):
                    return HttpResponse('  гавно собачье ')
                else:
                    self.object = form.save()
                    return super().form_valid(form)
        else:
            self.object = form.save()
            return super().form_valid(form)


class UpdateSession(UpdateView):
    model = Session
    form_class = SessionForm
    template_name = 'cinema_box_office/update_session.html'
    success_url = reverse_lazy('poster')


class DeleteSession(DeleteView):
    model = Session
    template_name = 'cinema_box_office/delete_session.html'
    success_url = reverse_lazy('poster')


class BuyTicket(CreateView, LoginRequiredMixin):
    model = Ticket
    http_method_names = ['post', 'get']
    success_url = '/'
    form_class = TicketForm
    template_name = 'cinema_box_office/user.html'
    success_url = reverse_lazy('poster')
    session = None

    login_url = '/authenticate/login/'

    def dispatch(self, request, *args, **kwargs):
        # userrt = self.request.user
        # sessi = self.session
        # import pdb
        # pdb.set_trace()
        if not request.user.is_authenticated:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        obj = form.save(commit=False)
        from cinema_box_office.models import Session
        session_from_form = form.data['session']
        movie_from_session = Session.objects.get(id=session_from_form)
        movie_cost = movie_from_session.ticket_price
        ticket_quantity = int(form.data['quantity'])
        user_bil = movie_cost * ticket_quantity
        self.request.user.wallet -= user_bil
        self.request.user.save()
        obj.user = self.request.user
        obj.session = movie_from_session
        cinema_hall = movie_from_session.cinema_hall
        cinema_hall.size -= ticket_quantity
        cinema_hall.save()
        print(obj.session.cinema_hall.size)
        obj.save()
        print(obj.session.cinema_hall.size)
        # import pdb
        # pdb.set_trace()

        return HttpResponseRedirect('/')


class CreateCinemaHall(CreateView, LoginRequiredMixin):
    model = CinemaHall
    template_name = 'cinema_box_office/create_cinema_hall.html'
    form_class = CinemaHallForm
    success_url = '/'
    login_url = '/authenticate/login/'

    def dispatch(self, request, *args, **kwargs):
        if (not request.user.is_authenticated) or ( not request.user.is_superuser):
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)


class CreateMovie(CreateView, LoginRequiredMixin):
    model = Movie
    template_name = 'cinema_box_office/create_movie.html'
    form_class = CreateMovieForm
    success_url = '/'
    login_url = '/authenticate/login/'

    def dispatch(self, request, *args, **kwargs):
        if (not request.user.is_authenticated) or ( not request.user.is_superuser):
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)


class BasketListView(ListView):
    model = Ticket
    context_object_name = 'tickets'
    template_name = 'cinema_box_office/basket.html'

    def get_queryset(self):
        return Ticket.objects.filter(user=self.request.user)