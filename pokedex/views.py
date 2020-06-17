from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, CreateView, DetailView

from pokedex.forms import AddForm
from .models import Pokemon


class PokemonListView(ListView):
    model = Pokemon


class PokemonDetailView(DetailView):
    model = Pokemon


def add_new_manually(request):
    if request.method == "POST":
        form = AddForm(request.POST)

        if form.is_valid():
            # time for magic ...
            p = Pokemon(name=form.cleaned_data['name'],
                        is_yellow=form.cleaned_data['is_yellow'])
            p.save()

            return HttpResponseRedirect('/')

    else:
        form = AddForm()

    return render(request, "pokedex/add.html", {'form': form})


class AddCreateView(CreateView):
    model = Pokemon
    fields = '__all__'


def check_date(request, pokemon_id):
    if request.method == "GET":
        pokemon = Pokemon.objects.get(id=pokemon_id)
        is_older_than_days = 7

        return render(request, "pokedex/check_date.html", {"is_older_than": pokemon.check_date(is_older_than_days)})
