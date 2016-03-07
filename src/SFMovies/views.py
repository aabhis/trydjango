from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import Http404

from SFMovies.serializers import UserSerializer
from SFMovies.serializers import FilmLocationsSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from SFMovies.models import FilmLocations
from django.http import HttpResponse

import json

# Create your views here.
def home(request):
    return render(request, "home.html", {})

def get_drugs(request):
    print request
    q = request.GET.get('term', '')
    print "Gets in is_ajax section... Input request term is : search term is : "+q
    #assert False, q
    drugs = FilmLocations.objects.filter(location__icontains = q )
    print drugs.query
    results = []
    for drug in drugs:
        drug_json = {}
        drug_json['title'] = drug.title
        drug_json['location'] = drug.location
        drug_json['latitude'] = drug.latitude
        
        drug_json['longitude'] = drug.longitude
        drug_json['city'] = drug.city
        drug_json['state'] = drug.state
        drug_json['county'] = drug.county
        drug_json['zipcode'] = drug.zipcode
        
        results.append(drug_json)
    data = json.dumps(results)
    print "Response data from for section : "+data
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)

class FilmLocationList(APIView):
    def get(self, request, format=None):
        films = FilmLocations.objects.all()
        serializer = FilmLocationsSerializer(films, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = FilmLocationsSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        films = self.get_object(pk)
        films.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class UserList(APIView):
    def get(self, request, format=None):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = UserSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class UserDetail(APIView):
    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        user = self.get_object(pk)
        user = UserSerializer(user)
        return Response(user.data)

    def put(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UserSerializer(user, data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)