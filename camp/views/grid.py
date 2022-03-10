from rest_framework import permissions, viewsets, status
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope
from camp.serializers import GridSerializer
from camp.models import Grid
from rest_framework.response import Response
from django.forms.models import model_to_dict


class GridViewsets(viewsets.ModelViewSet):
    permission = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    serializer_class = GridSerializer
    queryset = Grid.objects.all()
