from django.contrib import admin
from content.models import Content


# Register your models here.
class ContentAdmin(admin.ModelAdmin):

    class Meta():
        db_table = 'content'
    fields = ['title', 'full_text', 'state', 'created', 'cat_id', 'language']
    list_display = ['id', 'title', 'state', 'created', 'cat_id', 'likes', 'language']
    list_filter = ['cat_id', 'state', 'language']

admin.site.register(Content, ContentAdmin)
