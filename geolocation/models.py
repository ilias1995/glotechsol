from __future__ import unicode_literals

from django.db import models
from datetime import datetime, time, date

# Create your models here.
class Geolocation(models.Model):
    class Meta():
        db_table = 'visits'
    ip_address = models.CharField(max_length=255)
    country_name = models.CharField(max_length=255)
    country_code = models.CharField(max_length=50)
    visit_date = models.DateField(default=datetime.now, blank=True)

    def __str__(self):
        return self.country_name

class Views(models.Model):
    class Meta():
        db_table = 'views'
    ip_address = models.CharField(max_length=255)
    views_count = models.IntegerField()
    view_date = models.DateField(default=datetime.now, blank=True)