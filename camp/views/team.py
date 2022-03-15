from rest_framework import viewsets, status
from camp.serializers import TeamSerializer
from camp.models import Team
from rest_framework.response import Response
from django.forms.models import model_to_dict

    
class TeamViewsets(viewsets.ViewSet):
    permission = []
    serializer_class = TeamSerializer
    queryset = Team.objects.all()

    def create_team(self, request):
        serializer = TeamSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        team = serializer.create(request.data)

        return Response(model_to_dict(team), status=status.HTTP_201_CREATED)