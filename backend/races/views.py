from django.shortcuts import render

from django.http import Http404
from django.db.models import Q

from rest_framework.views import APIView
from rest_framework.response import Response 
from rest_framework.decorators import api_view

from .models import Category, Race

from .serializer import RaceSerializer
from .serializer import CategorySerializer
from races import serializer

class LatestRacesList(APIView):
    def get(self, request, format=None):
        races = Race.objects.all()[0:4]
        serializer = RaceSerializer(races, many=True)
        return Response(serializer.data)

class RacesDetail(APIView): 
    def get_object(self, category_slug, race_slug): 
        try:
            return Race.objects.filter(category__slug=category_slug).get(slug=race_slug)
        except Race.DoesNotExist:
            raise Http404

    def get(self, request, category_slug, race_slug, format=None):
        race = self.get_object(category_slug, race_slug)
        serializer = RaceSerializer(race)
        return Response(serializer.data)

class CategoryDetail(APIView):
    def get_object(self, category_slug): 
        try:
            return Category.objects.get(slug=category_slug)
        except Category.DoesNotExist:
            raise Http404

    def get(self, request, category_slug, format=None):
        category = self.get_object(category_slug)
        serializer = CategorySerializer(category)
        return Response(serializer.data)

@api_view(['POST'])
def search(request):
    query = request.data.get('query', '')

    if query:
        races = Race.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))
        serializer = RaceSerializer(races, many = True)
        return Response(serializer.data)

    else:
        return Response({"races": []})