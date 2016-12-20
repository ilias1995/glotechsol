from django.contrib import admin
from menu.models import Menu


# Register your models here.
class MenuAdmin(admin.ModelAdmin):

    class Meta():
        db_table = 'menu'
    fields = ['name', 'link', 'cat_id']
    list_display = ['name', 'link', 'cat_id']

admin.site.register(Menu, MenuAdmin)