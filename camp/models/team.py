from django.db import models
from camp.models.car import Car
from camp.models.pilot import Pilot
from camp.choices_points import DEFAULT_POINTS


class Team(models.Model):
    name = models.CharField(max_length=100)
    pilots = models.ManyToManyField(Pilot)
    car = models.OneToOneField(Car, on_delete=models.PROTECT, unique=True)
    points = models.CharField(choices=DEFAULT_POINTS, max_length=3, blank=True, default="not_point")

    def _a_str__(self) -> str:
        return self.name
