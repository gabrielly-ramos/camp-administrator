from rest_framework import status
from camp.serializers import CarSerializer
from camp.models import Car
from django.forms.models import model_to_dict
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

class CarViewset(ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

    # permission = []
    
    # def list(self, request):
    #     queryset = Car.objects.all()
    #     serializer = CarSerializer(queryset, many=True)
    #     return Response(serializer.data)
    
    # def create_car(self, request):
    #     serializer = CarSerializer(data=request.POST)
    #     serializer.is_valid(raise_exception=True)
    #     car = serializer.create(request.POST)

    #     return Response(model_to_dict(car), status=status.HTTP_201_CREATED)