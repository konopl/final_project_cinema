from django.contrib import admin
from cinema_box_office import models

# Register your models here.

admin.site.register(models.Movie)
admin.site.register(models.Session)
admin.site.register(models.CinemaHall)
admin.site.register(models.Ticket)
