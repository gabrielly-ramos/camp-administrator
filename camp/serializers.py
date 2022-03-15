from rest_framework import serializers
from camp.models import Pilot, Car, Grid, Team, pilot
from rest_framework import serializers
from django.contrib.auth.models import User, Group
from camp.choices_points import DEFAULT_POINTS
from django.shortcuts import get_object_or_404


class  PilotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pilot
        fields = '__all__'


class GridSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grid
        fields = '__all__'


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ("manufacturer", "car_model", "power", "weight", "pilot")
