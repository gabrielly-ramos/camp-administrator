from operator import imod
from django.db import models
from camp.models.car import Car
from camp.models.pilot import Pilot


class Team(models.Model):
    name = models.CharField(max_length=100)
    pilot = models.OneToOneField(Pilot, on_delete=models.PROTECT, unique=True)
    car = models.OneToOneField(Car, on_delete=models.PROTECT, unique=True)
