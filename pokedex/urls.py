from django.urls import path


from .views import PokemonListView

urlpatterns = [
    path('list/', PokemonListView.as_view()),
]
