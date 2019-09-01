from __future__ import unicode_literals

from django.db import models

# Create your models here.
class boardConf(models.Model):
    title = models.CharField(max_length=100)
    writer = models.CharField(max_length = 10)
    date = models.DateTimeField(auto_now_add=True)
    text = models.TextField()


    def __str__(self): 
        return self.title