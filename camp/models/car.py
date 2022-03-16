from django.db import models
from camp.models import Pilot


class Car(models.Model):
    manufacturer = models.CharField(max_length=150)    
    car_model = models.CharField(max_length=150)
    power = models.CharField(max_length=10)
    weight = models.CharField(max_length=10)
    pilots = models.ManyToManyField(Pilot, related_name="pilot")

    def __str__(self) -> str:
        return self.manufacturer