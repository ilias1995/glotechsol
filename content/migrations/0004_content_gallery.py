# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0003_auto_20161118_0309'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='gallery',
            field=models.BooleanField(default='true'),
        ),
    ]
