# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0002_auto_20161111_1047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='comments_text',
            field=models.TextField(verbose_name='Текст коментария:'),
        ),
        migrations.AlterField(
            model_name='content',
            name='full_text',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='content',
            name='state',
            field=models.BooleanField(default='true'),
        ),
    ]
