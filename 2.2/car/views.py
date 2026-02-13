from django.shortcuts import render
from .models import Car
from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView,RetrieveAPIView, UpdateAPIView
from .serializers import CarSerializer


# Create your views here.

class CarListAPIView(ListAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class CarCreateAPIView(CreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class CarDestroyAPIView(DestroyAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class CarUpdateAPIView(UpdateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class CarRetrieveAPIView(RetrieveAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer




