# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Color(models.Model):

    name = models.CharField(max_length=20)
    is_favorited = models.BooleanField(default=False)

    def __str__(self):
        return  self.name

    class Meta:
        ordering = ['name']
