from rest_framework import serializers

from pokedex.models import Pokemon


class PokemonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pokemon
        fields = ["id", "name", "date_added", "trainer"]