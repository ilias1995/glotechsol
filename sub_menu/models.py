from django.db import models
from django.contrib.auth.models import User
from menu.models import Menu
# Create your models here.
class Sub_Menu(models.Model):
    class Meta():
        db_table = 'sub_menu'
    name = models.CharField(max_length=255)
    link = models.CharField(max_length=255)
    cat_id = models.ForeignKey(Menu)

    def __str__(self):
        return self.name
