from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from shops.models import City
from shops.serializers import CitySerializer, CityStreetsSerializer


# Create your views here.

class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer


class CityDetail(APIView):
    def get_object(self, pk):
        try:
            city = City.objects.get(pk=pk)
            print(list(city.street_set.all()))
            return city
        except City.DoesNotExist:
            from django.http import Http404
            raise Http404

    def get(self, request, pk):
        city = self.get_object(pk)
        serializer = CityStreetsSerializer(city)
        print(serializer.data)
        return Response(serializer.data)
