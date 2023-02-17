from rest_framework import serializers
from .models import house

class HouseSerializer(serializers.ModelSerializer):
    class Meta:
        model=house
        fields="__all__"