# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category_menu', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('link', models.CharField(max_length=255)),
                ('cat_id', models.ForeignKey(to='category_menu.Category_Menu')),
            ],
            options={
                'db_table': 'menu',
            },
        ),
    ]
