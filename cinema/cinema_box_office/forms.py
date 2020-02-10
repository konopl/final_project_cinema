from django.forms import ModelForm, DateInput, TimeInput
from .models import Session


class SessionForm(ModelForm):
    class Meta:
        # widgets = {
        #     'rental_start_at': DateInput(),
        #     'start_at': TimeInput,
        # }
        model = Session
        fields = [
            'name',
            'start_at',
            'end_at',
            'rental_start_at',
            'rental_end_at',
            'ticket_price',
            'cinema_hall',
            'movie',
            ]