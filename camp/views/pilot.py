from rest_framework import status
from camp.serializers import PilotSerializer

from camp.models import Pilot, pilot
from rest_framework.response import Response
from django.forms.models import model_to_dict
from rest_framework.viewsets import ModelViewSet


class PilotViewset(ModelViewSet):
    queryset = Pilot.objects.all()
    serializer_class = PilotSerializer
