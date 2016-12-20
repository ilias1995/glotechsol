from django.db import models
from django.contrib.auth.models import User
from category_menu.models import Category_Menu

# Create your models here.
class Menu(models.Model):
    class Meta():
        db_table = 'menu'
    name = models.CharField(max_length=255)
    link = models.CharField(max_length=255)
    cat_id = models.ForeignKey(Category_Menu)

    def __str__(self):
        return self.name
