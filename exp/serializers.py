from rest_framework import serializers
from .models import cab,Hotels,lodge,places
class apicab(serializers.ModelSerializer):
    class Meta:
        model=cab
        fields=('name','desc')
        
class apiHotels(serializers.ModelSerializer):
    class Meta:
        model=Hotels
        fields=('location','type','image','name','number','rating')
        
class apiplaces(serializers.ModelSerializer):
    class Meta:
        model=places
        fields=('place_name','place_desc','location')
        
class apilodge(serializers.ModelSerializer):
    class Meta:
        model=lodge
        fields=('name','contacts','address','typeOfroom','total_rooms')
        