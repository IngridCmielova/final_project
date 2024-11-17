from django.db import models
from django.contrib.auth.models import User


class Reservation(models.Model):
    date = models.DateField()
    time = models.TimeField()
    procedure = models.ForeignKey('Procedure', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('date', 'time', 'procedure')


class Procedure(models.Model):
    name = models.CharField(max_length=100)
    duration = models.DurationField()
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
