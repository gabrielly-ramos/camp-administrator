from rest_framework import status
from camp.serializers import CarSerializer
from camp.models import Car
from django.forms.models import model_to_dict
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

class CarViewset(ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

