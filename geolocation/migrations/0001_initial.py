# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Geolocation',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('ip_address', models.CharField(max_length=255)),
                ('country_name', models.CharField(max_length=255)),
                ('country_code', models.CharField(max_length=50)),
                ('visit_date', models.DateField(blank=True, default=datetime.datetime.now)),
            ],
            options={
                'db_table': 'visits',
            },
        ),
        migrations.CreateModel(
            name='Views',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('ip_address', models.CharField(max_length=255)),
                ('views_count', models.IntegerField()),
                ('view_date', models.DateField(blank=True, default=datetime.datetime.now)),
            ],
            options={
                'db_table': 'views',
            },
        ),
    ]
