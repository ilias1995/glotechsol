# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '__first__'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('language', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comments_date', models.DateField()),
                ('comments_text', models.TextField(verbose_name=b'\xd0\xa2\xd0\xb5\xd0\xba\xd1\x81\xd1\x82 \xd0\xba\xd0\xbe\xd0\xbc\xd0\xb5\xd0\xbd\xd1\x82\xd0\xb0\xd1\x80\xd0\xb8\xd1\x8f:')),
            ],
            options={
                'db_table': 'comments',
            },
        ),
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('full_text', models.TextField()),
                ('state', models.BooleanField(default=b'true')),
                ('created', models.DateField()),
                ('likes', models.IntegerField(default=0)),
                ('hints', models.IntegerField()),
                ('cat_id', models.ForeignKey(to='categories.Category')),
                ('language', models.ForeignKey(to='language.language')),
            ],
            options={
                'db_table': 'content',
            },
        ),
        migrations.AddField(
            model_name='comments',
            name='comments_article',
            field=models.ForeignKey(to='content.Content'),
        ),
        migrations.AddField(
            model_name='comments',
            name='comments_from',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
