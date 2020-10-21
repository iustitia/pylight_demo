from rest_framework.generics import ListAPIView
from rest_framework import viewsets

from pokedex.models import Pokemon
from pokedex.serializers import PokemonSerializer


class PokemonListAPIView(ListAPIView):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer
    http_method_names = ['get']


class PokemonListAPIViewSet(viewsets.ModelViewSet):
    serializer_class = PokemonSerializer
    queryset = Pokemon.objects.all()
