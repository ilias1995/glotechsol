from django.contrib import admin
from language.models import language


class LanguageAdmin(admin.ModelAdmin):
    fields = ['language']
    list_display = ['language']
admin.site.register(language, LanguageAdmin)