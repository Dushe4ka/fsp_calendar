from django.db import models


class SportEvents(models.Model):
    event_id = models.IntegerField(blank=True, null=True)
    type = models.CharField(blank=True, null=True)
    sport = models.CharField(blank=True, null=True)
    discip = models.CharField(blank=True, null=True)
    program = models.CharField(blank=True, null=True)
    gender_age = models.CharField(blank=True, null=True)
    date_start = models.DateField(blank=True, null=True)
    date_end = models.DateField(blank=True, null=True)
    country = models.CharField(blank=True, null=True)
    subject = models.CharField(blank=True, null=True)
    city = models.CharField(blank=True, null=True)
    participants = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sport_events'

    def __str__(self):
        return f'{self.type} ({self.date_start}-{self.date_end})'
