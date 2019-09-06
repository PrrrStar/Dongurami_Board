# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Board_DB(models.Model):
    title = models.CharField(max_length=400)
    tag = models.CharField(max_length=50)
    writer = models.CharField(max_length=120, null=True, default='')
    contents = models.TextField(null=True, default='')
    date = models.DateTimeField(auto_now_add=True)
    hits = models.PositiveIntegerField(default=0)
    pwd = models.CharField(max_length=15, null=True, default='')
    
    def __unicode__(self):
        return self.title

    @property
    def hit_value(self):
        self.hits = self.hits +1
        self.save()

class Comment_DB(models.Model):
    c_post = models.ForeignKey('Board_DB',related_name='comments', on_delete=models.CASCADE)
    c_writer = models.CharField(max_length=10, default='익명')
    c_contents = models.TextField(null=False, default='')
    c_date = models.DateTimeField(auto_now_add=True)
    c_like = models.IntegerField(default=0)
    c_dislike = models.IntegerField(default=0)

    def __str__(self):
        return self.c_contents
