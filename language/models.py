from django.db import models

class language(models.Model):
    class Meta():
        db_table = 'language'
    language = models.CharField(max_length=255)
    fields = ['id', 'language']
    list_display = ['id', 'language']

    def __str__(self):
        return self.language

