from django.forms import ModelForm, DateInput, TimeInput
from .models import Session, CinemaHall


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
        # widgets = {
        #     'rental_start_at': forms.DateField(widget=DateInput),
        # }


class CinemaHallForm(ModelForm):
    class Meta:
        model = CinemaHall
        fields = (
            'name',
            'size',
        )
