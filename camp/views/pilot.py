from rest_framework import viewsets, status
from camp.serializers import PilotSerializer

from camp.models import Pilot
from rest_framework.response import Response
from django.forms.models import model_to_dict


class PilotViewsets(viewsets.ViewSet):
    permission = []
    serializer_class = PilotSerializer

    def list(self, request):
        queryset = Pilot.objects.all()
        serializer = PilotSerializer(queryset, many=True)
        return Response(serializer.data)


    def create_pilot(self, request):
        serializer = PilotSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        pilot = serializer.create(request.data)

        return Response(model_to_dict(pilot), status=status.HTTP_201_CREATED)

    def update_pilot(self, request, pk):
        pilot_object = self.get_object()
        data = request.data

        # pilot_id = Pilot.objects.get(name=data["name"])
        pilot_object.name = data["name"]
        pilot_object.id_psn = data["id_psn"]
        pilot_object.number = data["number"]
        pilot_object.points = data["points"]

        pilot_object.save()

        serializer = PilotSerializer(data=model_to_dict(pilot_object))

        serializer.is_valid(raise_exception=True)
        

        return Response(serializer.data)