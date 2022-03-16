from pyexpat import model
from django.db import models
from camp.models import Car, Pilot, Team
from camp.choices_points import DEFAULT_POINTS


class Grid(models.Model):
    name = models.CharField(max_length=30)
    pilots = models.ManyToManyField(Pilot)
    cars = models.ManyToManyField(Car)
    teams = models.ManyToManyField(Team)
    

    def __str__(self) -> str:
        return self.name