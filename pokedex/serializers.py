from rest_framework import serializers

from pokedex.models import Pokemon


class PokemonSimpleSerializer(serializers.Serializer):
    name = serializers.CharField()
    is_yellow = serializers.BooleanField()
    date_added = serializers.DateField()


class PokemonModelSerializer(serializers.ModelSerializer):
    """
    All fields are based on model fields automatically
    """
    #type = serializers.StringRelatedField(many=True)
    type = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='name'
     )

    class Meta:
        model = Pokemon
        fields = ["id", "name", "date_added", "trainer", "type"]
