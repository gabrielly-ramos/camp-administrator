from rest_framework import permissions, viewsets, status
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, TokenHasScope
from camp.serializers import ( 
    PilotSerializer, 
    CreatePilotSerializer)

from camp.models import Pilot
from rest_framework.response import Response
from django.forms.models import model_to_dict


class PilotViewsets(viewsets.ModelViewSet):
    permission = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    serializer_class = PilotSerializer
    queryset = Pilot.objects.all()

    def create_pilot(self, request):
        serializer = CreatePilotSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        pilot = serializer.create(request.data)

        return Response(model_to_dict(pilot), status=status.HTTP_201_CREATED)
