from django.db import models
from camp.choices_points import DEFAULT_POINTS


class Pilot(models.Model):
    name = models.CharField(max_length=30)
    id_psn = models.CharField(max_length=30)
    number = models.IntegerField()
    points = models.CharField(choices=DEFAULT_POINTS, max_length=3, blank=True, default="not_point")

    def __str__(self) -> str:
        return self.name