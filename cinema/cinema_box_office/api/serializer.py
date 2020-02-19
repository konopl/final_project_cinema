from rest_framework import serializers
from cinema_box_office.models import Session


class SessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Session
        fields = ['name',
                  'start_at',
                  'end_at',
                  'rental_start_at',
                  'rental_end_at',
                  'ticket_price',
                  'cinema_hall',
                  'movie',
                  ]
