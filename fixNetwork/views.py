from django.shortcuts import render
from rest_framework import viewsets
from . models import FixNetwork
from .serializers import FixNetworkSerializer

# Create your views here.

class FixNetworkView(viewsets.ModelViewSet):
    queryset = FixNetwork.objects.all()
    serializer_class = FixNetworkSerializer

