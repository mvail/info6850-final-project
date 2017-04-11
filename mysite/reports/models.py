from __future__ import unicode_literals

from django.db import models

# Create your models here.
# -*- coding: utf-8 -*-

class Patent(models.Model):
    pid = models.PositiveIntegerField()
    pid.primary_key=True
    ptext = models.CharField(max_length=2100000000)
    uspc = models.PositiveIntegerField()
    claims = models.PositiveIntegerField()
    inventors = models.PositiveIntegerField()
    week = models.PositiveIntegerField()

class Keywords(models.Model):
    word = models.CharField(max_length=1000)
    word_count = models.PositiveIntegerField()
    week = models.PositiveIntegerField()

class Uspc(models.Model):
    week = models.PositiveIntegerField()
    uspc = models.PositiveIntegerField()
    patent_count = models.PositiveIntegerField()