from django.contrib import admin
from sub_menu.models import Sub_Menu


# Register your models here.
class SubMenuAdmin(admin.ModelAdmin):

    class Meta():
        db_table = 'submenu'
    fields = ['name', 'link', 'cat_id']
    list_display = ['name', 'link', 'cat_id']
    list_filter = ['cat_id']

admin.site.register(Sub_Menu, SubMenuAdmin)

