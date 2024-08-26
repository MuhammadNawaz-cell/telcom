from rest_framework import serializers
from .models import FixNetwork

class FixNetworkSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FixNetwork
        fields = ('id','url', 'router', 'm14', 'm10')
