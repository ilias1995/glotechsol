from django.contrib import admin
from category_menu.models import Category_Menu
# Register your models here.

class AdminCategory_Menu(admin.ModelAdmin):

    class Meta():
        db_table = 'category_menu'
    fields = ['name', 'link', 'language', 'position']
    list_display = ['name', 'link', 'language', 'position']


admin.site.register(Category_Menu, AdminCategory_Menu)