from rest_framework import serializers
from camp.models import Pilot, Car, Grid, Team
from rest_framework import serializers
from django.contrib.auth.models import User, Group
from camp.choices_points import DEFAULT_POINTS
from django.shortcuts import get_object_or_404


class  PilotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pilot
        fields = '__all__'


class GridSerializer(serializers.ModelSerializer):
    pilots = serializers.PrimaryKeyRelatedField(many=True, queryset=Pilot.objects.all())
    cars = serializers.PrimaryKeyRelatedField(many=True, queryset=Car.objects.all())
    teams = serializers.PrimaryKeyRelatedField(many=True, queryset=Team.objects.all())

    class Meta:
        model = Grid
        fields = '__all__'
        depth = 1


class TeamSerializer(serializers.ModelSerializer):
    pilots = serializers.PrimaryKeyRelatedField(many=True, queryset=Pilot.objects.all())
    class Meta:
        model = Team
        fields = '__all__'


class CarSerializer(serializers.ModelSerializer):
    pilots = serializers.PrimaryKeyRelatedField(many=True, queryset=Pilot.objects.all())
    class Meta:
        model = Car
        fields = '__all__'
        depth = 1