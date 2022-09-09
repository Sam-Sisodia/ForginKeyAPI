
from dataclasses import fields
from rest_framework import serializers
from . models import *




class stateSerializer(serializers.ModelSerializer):
    class Meta:
        model= State
        fields = ['State_name','number_of_cities','number_of_schools','number_of_stadiums','state_image']




class citySerializer(serializers.ModelSerializer):
    class Meta:
        model= City
        fields = ['city_name','city_area','city_population','state']





class townSerializer(serializers.ModelSerializer):
    class Meta:
        model= Town
        fields= ['town_name','town_code','town_population','city_name']