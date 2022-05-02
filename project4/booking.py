from django.contrib.postgres.constraints import ExclusionConstraint
from django.contrib.postgres.fields import DateTimeRangeField, RangeOperators
from django.db import models
from django.db.models import Q


class Table(models.Model):
    number = models.IntegerField()


class Reservation(models.Model):
    table = models.ForeignKey('Table', on_delete=models.CASCADE)
    timespan = DateTimeRangeField()
    cancelled = models.BooleanField(default=False)

    class Meta:
        constraints = [
            ExclusionConstraint(
                name='exclude_overlapping_reservations',
                expressions=[
                    ('timespan', RangeOperators.OVERLAPS),
                    ('table', RangeOperators.EQUAL),
                ],
                condition=Q(cancelled=False),
            ),
        ]