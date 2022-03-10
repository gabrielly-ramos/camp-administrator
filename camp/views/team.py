from rest_framework import permissions, viewsets, status
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope
from camp.serializers import TeamSerializer
from camp.models import Team
from rest_framework.response import Response
from django.forms.models import model_to_dict

    
class TeamViewsets(viewsets.ModelViewSet):
    permission = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    serializer_class = TeamSerializer
    queryset = Team.objects.all()

    