from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    wallet = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    #def __init__(self):


