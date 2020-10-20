from django.urls import path

from .models import Pokemon
from .views import PokemonListView, PokemonDetailView, add_new_manually, AddCreateView, check_date
from .viewsets import PokemonListAPIView

urlpatterns = [
    path('', PokemonListView.as_view()),
    path('<int:pk>/', PokemonDetailView.as_view(), name="detail-view"),


    path('add_manually', add_new_manually),
    path('add_detail_view', AddCreateView.as_view(), name='add-create-view'),
    path('check_if_older/<int:pokemon_id>/', check_date),
    path('api/pokemons/', PokemonListAPIView.as_view(queryset=Pokemon.objects.all()), name="pokemons"),
]
