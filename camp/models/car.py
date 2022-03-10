from pyexpat import model
from django.db import models
from camp.models.pilot import Pilot


class Car(models.Model):
    manufacturer = models.CharField(max_length=150)
    car_model = models.CharField(max_length=150)
    power = models.CharField(max_length=10)
    weight = models.CharField(max_length=10)
    pilot = models.OneToOneField(Pilot, on_delete=models.PROTECT, unique=True)