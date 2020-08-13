from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import Dessert

class DessertSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Dessert
        fields = ('identifier', 'category', 'description', 'identification', 'initdate', 'productname', 'value')

