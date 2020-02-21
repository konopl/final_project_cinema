from django.forms import ModelForm, DateInput, TimeInput, DateTimeInput
from .models import Session, CinemaHall, Ticket, Movie


class SessionForm(ModelForm):
    class Meta:
        model = Session
        fields = (
            'name',
            'start_at',
            'end_at',
            'rental_start_at',
            'rental_end_at',
            'ticket_price',
            'cinema_hall',
            'movie',
        )
        widgets = {
            'rental_start_at': DateInput(format='%d/%m/%Y', attrs={
                'class': 'form-control', 'placeholder': 'Select a date', 'type': 'date'}),
            'rental_end_at': DateInput(format='%d/%m/%Y', attrs={
                'class': 'form-control', 'placeholder': 'Select a date', 'type': 'date'}),
            # 'start_at': DateTimeInput(format="%d/%m/%Y %H:%M:%S", attrs={
            #     'placeholder': "DD/MM/YYYY HH:MM:SS",
            #     'type': 'datetime'}),
            # 'end_at': DateTimeInput(format="%d/%m/%Y %H:%M:%S", attrs={
            #     'placeholder': "DD/MM/YYYY HH:MM:SS",
            #     'type': 'datetime'})
        }


class CinemaHallForm(ModelForm):
    class Meta:
        model = CinemaHall
        fields = (
            'name',
            'size',
        )


class TicketForm(ModelForm):
    class Meta:
        model = Ticket
        fields = (
            'quantity',        )


class CreateMovieForm(ModelForm):
    class Meta:
        model = Movie
        fields = (
            'name',
        )
