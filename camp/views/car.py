from rest_framework import viewsets, status
from camp.serializers import CarSerializer
from camp.models import Car
from django.forms.models import model_to_dict
from rest_framework.response import Response

class CarViewsets(viewsets.ModelViewSet):
    permission = []
    serializer_class = CarSerializer
    
    def get_queryset(self):
        return Car.objects.all()

    
    def create_car(self, request):
        serializer = CarSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        car = serializer.create(request.data)

        return Response(model_to_dict(car), status=status.HTTP_201_CREATED)