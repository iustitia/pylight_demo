from django.db import models


class Trainer(models.Model):
    name = models.CharField(max_length=200)


class Pokemon(models.Model):
    name = models.CharField(max_length=200)
    is_yellow = models.BooleanField(default=False)
    # trainer = models.ForeignKey(Trainer, on_delete=None)

    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return "{}, {}".format(self.name, self.is_yellow)

    def get_absolute_url(self):
        return '/%d' % self.id
