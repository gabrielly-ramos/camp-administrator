from rest_framework import viewsets, status
from camp.serializers import TeamSerializer
from camp.models import Team
from rest_framework.response import Response
from django.forms.models import model_to_dict
from rest_framework.viewsets import ModelViewSet

    
class TeamViewset(ModelViewSet):    
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
