# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('language', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category_Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('link', models.CharField(max_length=255)),
                ('position', models.IntegerField()),
                ('language', models.ForeignKey(to='language.language')),
            ],
            options={
                'db_table': 'category_menu',
            },
        ),
    ]
