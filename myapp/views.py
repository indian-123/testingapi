from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import house
from .serializers import HouseSerializer

class HouseList(generics.ListCreateAPIView):
    queryset = house.objects.all()
    serializer_class = HouseSerializer
    # return HttpResponse("hi")

class HouseDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = house.objects.all()
    serializer_class = HouseSerializer