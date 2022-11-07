from rest_framework import viewsets, serializers

from shops.models import City


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ('name')



