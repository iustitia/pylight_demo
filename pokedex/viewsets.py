from rest_framework.generics import ListAPIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from pokedex.models import Pokemon
from pokedex import serializers


class BasicEndpoint(APIView):
    def get(self, request, format=None):
        return Response("OK")


class PokemonSimpleListAPIView(ListAPIView):
    """
    Uses generic ListAPIView, but shows only one endpoint for listing
    """
    queryset = Pokemon.objects.all()
    serializer_class = serializers.PokemonSimpleSerializer


class PokemonListAPIView(ListAPIView):
    """
    Uses generic ListAPIView, but shows only one endpoint for listing
    """
    queryset = Pokemon.objects.all()
    serializer_class = serializers.PokemonModelSerializer


class PokemonAPIViewSet(viewsets.ModelViewSet):
    """
    Uses viewsets that automatically create CRUD style endpoint for a model
    """
    serializer_class = serializers.PokemonModelSerializer
    queryset = Pokemon.objects.all()
