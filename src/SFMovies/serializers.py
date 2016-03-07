from django.contrib.auth.models import User
from SFMovies.models import FilmLocations
from rest_framework import serializers
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email')
        
class FilmLocationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = FilmLocations
        fields = ('title','location','state','city','latitude','longitude','accuracyscore','accuracytype','number','street','city','state','county','zipcode')