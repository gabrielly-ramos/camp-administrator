from rest_framework import serializers
from camp.models import Pilot, Car, Grid, Team
from rest_framework import serializers
from django.contrib.auth.models import User, Group
from camp.choices_points import DEFAULT_POINTS
from django.shortcuts import get_object_or_404


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "email", "first_name", "last_name")


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ("name", )

class PilotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pilot
        fields = ("name", "id_psn", "number", "points",)

class CreatePilotSerializer(serializers.Serializer):
    
    def create(self, validated_data):
        pilot = Pilot(
            name=validated_data.get("name"),
            id_psn=validated_data.get("id_psn"),
            number=validated_data.get("number"),
            points=validated_data.get("points"),

        )
        pilot.save()
        return pilot


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'


class CreateCarSerializer(serializers.Serializer):
    def create(self, validated_data):

        pilot_id = get_object_or_404(Pilot, id=validated_data.get("pilot"))
        car = Car(
            manufacturer = validated_data.get("manufacturer"),
            car_model = validated_data.get("car_model"),
            power = validated_data.get("power"),
            weight = validated_data.get("weight"),
            pilot = pilot_id,
        )

        car.save()
        return car

class GridSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grid
        fields = '__all__'

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'