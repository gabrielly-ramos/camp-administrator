from django.db import models
from camp.models import Car, Pilot, Team
from camp.choices_points import DEFAULT_POINTS


class Grid(models.Model):
    pilots = models.OneToOneField(Pilot, on_delete=models.PROTECT, unique=True)
    cars = models.OneToOneField(Car, on_delete=models.PROTECT, unique=True)
    teams = models.OneToOneField(Team, on_delete=models.PROTECT, unique=True)
    points = models.CharField(choices=DEFAULT_POINTS, max_length=3, blank=True)
