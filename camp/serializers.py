from rest_framework import serializers
from camp.models import Pilot, Car, Grid, Team
from rest_framework import serializers


class PilotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pilot
        fields = '__all__'

    
    def update(self, instance, validated_data):
        points = int(instance.points)
        if validated_data.get("points"):
            instance.points = points + validated_data.get("points")
        instance.save()

        return instance


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

    
    def update(self, instance, validated_data):
        if validated_data.get("points"):
            instance.points = int(instance.points) + validated_data.get("points")
        instance.save()

        return instance


class CarSerializer(serializers.ModelSerializer):
    pilots = serializers.PrimaryKeyRelatedField(many=True, queryset=Pilot.objects.all())
    class Meta:
        model = Car
        fields = '__all__'
        depth = 1