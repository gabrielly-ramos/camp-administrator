from rest_framework import permissions, viewsets, status
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope
from camp.serializers import CarSerializer, CreateCarSerializer
from camp.models import Car
from django.forms.models import model_to_dict
from rest_framework.response import Response

class CarViewsets(viewsets.ModelViewSet):
    permission = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    serializer_class = CarSerializer
    
    def get_queryset(self):
        return Car.objects.all()

    
    def create_car(self, request):
        serializer = CreateCarSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        car = serializer.create(request.data)

        return Response(model_to_dict(car), status=status.HTTP_201_CREATED)