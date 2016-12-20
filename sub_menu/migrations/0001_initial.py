# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sub_Menu',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=255)),
                ('link', models.CharField(max_length=255)),
                ('cat_id', models.ForeignKey(to='menu.Menu')),
            ],
            options={
                'db_table': 'sub_menu',
            },
        ),
    ]
