from django.shortcuts import render
from rest_framework import viewsets

from shops.models import City
from shops.serializers import CitySerializer


# Create your views here.

class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer


