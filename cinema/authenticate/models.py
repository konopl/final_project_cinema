from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    wallet = models.DecimalField(max_digits=5, decimal_places=5, blank=True, null=True)


