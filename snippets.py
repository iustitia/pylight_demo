from pokedex.models import Pokemon

pokemon_list = [Pokemon(name="Pikachu", is_yellow=True),
                Pokemon(name="Bulbasaur", is_yellow=False),
                Pokemon(name="Eevee", is_yellow=False),
                Pokemon(name="Psyduck", is_yellow=True),
                Pokemon(name="Squirtle", is_yellow=False)]

[p.save() for p in pokemon_list]

######

speed = models.IntegerField(null=True)
series = models.IntegerField(default=1)
date_added = models.DateField(null=True)

######


from datetime import datetime
pokemon_list = [Pokemon(name="Magikarp", is_yellow=False, date_added=datetime(2015, 7, 13)),
                Pokemon(name="Pidgey", is_yellow=False, date_added=datetime(2017, 1, 24))]

[p.save() for p in pokemon_list]

######

Pokemon.objects.filter(date_added__year=2015)


######

class Trainer(models.Model):
    name = models.CharField(max_length=200)


class Pokemon:
    # ....
    trainer = models.ForeignKey(Trainer, on_delete=models.DO_NOTHING, blank=True, null=True)