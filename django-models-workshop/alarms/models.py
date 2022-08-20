from django.db import models
from measurements.models import Measurement


class Alarm(models.Model):
    name = models.CharField(max_length=50, default="Undefined Alarm")
    measurement = models.ManyToManyField(Measurement)

    def __str__(self):
        return '{}'.format(self.name)
