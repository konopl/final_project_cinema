from django.db import models
from authenticate.models import User

# Create your models here.

HALL_COLOR = (
    ('green', 'Green'),
    ('red', 'Red'),
    ('blue', 'Blue')
)


class CinemaHall(models.Model):
    name = models.CharField(choices=HALL_COLOR, max_length=100)
    size = models.IntegerField()

    def __str__(self):
        return f'{self.name}'


class Movie(models.Model):
    name = models.CharField(max_length=200)
    # session = models.OneToOneField(Session, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}'


class Session(models.Model):
    name = models.CharField(max_length=200)
    start_at = models.DateTimeField()  # не уверен что это правильное решение
    end_at = models.DateTimeField()
    rental_start_at = models.DateTimeField()
    rental_end_at = models.DateTimeField()
    ticket_price = models.DecimalField(max_digits=4, decimal_places=2)
    cinema_hall = models.ForeignKey(CinemaHall, on_delete=models.CASCADE)
    movie = models.OneToOneField(Movie, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}'


class Ticket(models.Model):
    quantity = models.IntegerField
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.session}'


