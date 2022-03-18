from rest_framework import status
from camp.serializers import GridSerializer
from camp.models import Grid
from rest_framework.response import Response
from django.forms.models import model_to_dict
from rest_framework.viewsets import ModelViewSet


class GridViewset(ModelViewSet):    
    queryset = Grid.objects.all()
    serializer_class = GridSerializer
