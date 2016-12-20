from __future__ import unicode_literals

from django.db import models
from language.models import language

# Create your models here.
class Category_Menu(models.Model):
    class Meta():
        db_table = 'category_menu'
    name = models.CharField(max_length=255)
    link = models.CharField(max_length=255)
    position = models.IntegerField()
    language = models.ForeignKey(language)

    def __str__(self):
        return self.name
