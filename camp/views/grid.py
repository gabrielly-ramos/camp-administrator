from rest_framework import viewsets, status
from camp.serializers import GridSerializer
from camp.models import Grid
from rest_framework.response import Response
from django.forms.models import model_to_dict


class GridViewsets(viewsets.ModelViewSet):
    permission = []
    serializer_class = GridSerializer
    queryset = Grid.objects.all()

    def create_grid(self, request):
        serializer = GridSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        grid = serializer.create(request.data)

        return Response(model_to_dict(grid), status=status.HTTP_201_CREATED)