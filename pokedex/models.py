from django.db import models

# Create your models here.


class Pokemon(models.Model):
    name = models.CharField(max_length=200)
    is_yellow = models.BooleanField()

    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return self.name
