# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from categories.models import Category
from language.models import language
from ckeditor.fields import RichTextField


# Create your models here.

class Content(models.Model):
    class Meta():
        db_table = "content"
    title = models.CharField(max_length=200)
    full_text = RichTextField()
    state = models.BooleanField(default='true')
    gallery = models.BooleanField(default='true')
    created = models.DateField()
    likes = models.IntegerField(default=0)
    cat_id = models.ForeignKey(Category)
    language = models.ForeignKey(language)
    hints = models.IntegerField(default=0)

    def __str__(self):
        return self.title

class Comments(models.Model):
    class Meta():
        db_table = 'comments'
    comments_date = models.DateField()
    comments_text = models.TextField(verbose_name="Текст коментария:")
    comments_article = models.ForeignKey(Content)
    comments_from = models.ForeignKey(User)


