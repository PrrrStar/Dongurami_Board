# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class myDB(models.Model):
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
