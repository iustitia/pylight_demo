from rest_framework.generics import ListAPIView

from pokedex.models import Pokemon
from pokedex.serializers import PokemonSerializer


class PokemonListAPIView(ListAPIView):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer
    http_method_names = ['get']
