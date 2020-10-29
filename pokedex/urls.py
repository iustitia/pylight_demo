from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns

from .models import Pokemon
from . import views
from . import viewsets

urlpatterns = [
    path('pokemon', views.PokemonListView.as_view()),
    path('<int:pk>/', views.PokemonDetailView.as_view(), name="detail-view"),

    path('add_manually', views.add_new_manually),
    path('add_detail_view', views.AddCreateView.as_view(), name='add-create-view'),
    path('check_if_older/<int:pokemon_id>/', views.check_date),


    # api
    path('api/v1/basic/', viewsets.BasicEndpoint.as_view()),

    # with non-model serializer
    path('api/v1/pokemon/', viewsets.PokemonSimpleListAPIView.as_view(queryset=Pokemon.objects.all()), name="pokemons"),

    # with model serializer
    path('api/v2/pokemon/', viewsets.PokemonListAPIView.as_view(queryset=Pokemon.objects.all()), name="pokemons"),

]

urlpatterns = format_suffix_patterns(urlpatterns)

# with viewsets
router = DefaultRouter()
router.register(r'api/v3/pokemon', viewsets.PokemonAPIViewSet)

urlpatterns += router.urls
