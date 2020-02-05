from django.db import models

# Create your models here.

HALL_COLOR = (
    ('green', 'Green'),
    ('red', 'Red'),
    ('blue', 'Blue')
)


class CinemaHall(models.Model):
    name = models.CharField(choices=HALL_COLOR)
    size = models.IntegerField(max_length=200)


class Session(models.Model):
    start_at = models.DateTimeField()  # не уверен что это правильное решение
    end_at = models.DateTimeField()
    rental_start_at = models.DateTimeField()
    rental_end_at = models.DateTimeField()
    ticket_price = models.DecimalField(max_digits=3)
    cinema_hall = models.ForeignKey(CinemaHall, on_delete=models.CASCADE)
