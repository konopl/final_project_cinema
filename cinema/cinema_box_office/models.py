from django.db import models
from authenticate.models import User

# Create your models here.

# HALL_COLOR = (
#     ('green', 'Green'),
#     ('red', 'Red'),
#     ('blue', 'Blue')
# )


class CinemaHall(models.Model):
    name = models.CharField(max_length=100)
    size = models.IntegerField()

    def __str__(self):
        return f'{self.name} - {self.size}'


class Movie(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.name}'


class Session(models.Model):
    name = models.CharField(max_length=200)
    start_at = models.DateTimeField()  # не уверен что это правильное решение
    end_at = models.DateTimeField()
    rental_start_at = models.DateTimeField()
    rental_end_at = models.DateTimeField()
    ticket_price = models.DecimalField(max_digits=5, decimal_places=2)
    cinema_hall = models.ForeignKey(CinemaHall, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    # rent_start = models.DateField(null=True)
    # rental_duration = models.DurationField()
    # movie_duration = models.DurationField()

    class Meta:
        ordering = ['-start_at', ]

    def __str__(self):
        return f'{self.name}'


class Ticket(models.Model):
    quantity = models.IntegerField(null=True)
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.session}'

    # def get_cost(self):
    #     return self.session.price * self.amount

    # def buy(self, price, quantity, session):
    #     # buy and add to total_bonuses
    #     self.buyer.bonuses -= price * int(quantity)
    #     self.buyer.save()
    #     self.session.available_seats -= int(quantity)
    #     self.session.save()
    #     self.buyer.total_bonuses += price * int(quantity)
    #     self.buyer.save()

    # def __str__(self):
    #     return f"Ticket of film '{self.session.film.name}' at {self.session.time_from}"
