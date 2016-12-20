from django.contrib import admin
from categories.models import Category


# Register your models here.
class CategoryAdmin(admin.ModelAdmin):

    class Meta():
        db_table = 'languages'
    fields = ['category_name']
    list_display = ['id', 'category_name']

admin.site.register(Category, CategoryAdmin)