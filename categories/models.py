from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Category(models.Model):
    class Meta():
        db_table = 'category'
    category_name = models.CharField(max_length=255)

    def __str__(self):
        return self.category_name

