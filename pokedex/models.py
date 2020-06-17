from django.db import models


class Trainer(models.Model):
    name = models.CharField(max_length=200)


class Pokemon(models.Model):
    name = models.CharField(max_length=200)
    is_yellow = models.BooleanField(default=False)
    date_added = models.DateField(null=True, blank=True, auto_now=True)
    trainer = models.ForeignKey(Trainer, on_delete=None, null=True, blank=True)

    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return "{}, {}".format(self.name, self.is_yellow)

    def get_absolute_url(self):
        return '/%d' % self.id

    def get_trainer_name(self):
        return self.trainer.name

    def check_date(self, days):
        from datetime import timedelta, date
        return date.today() - self.date_added > timedelta(days=days)
