# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Adult(models.Model):
    id = models.IntegerField(primary_key=True)
    age = models.IntegerField(blank=True, null=True)
    workclass = models.TextField(blank=True, null=True)  # This field type is a guess.
    fnlwgt = models.IntegerField(blank=True, null=True)
    education = models.TextField(blank=True, null=True)
    education_num = models.TextField(blank=True, null=True)
    martial_status = models.TextField(blank=True, null=True)
    occupation = models.TextField(blank=True, null=True)
    relationship = models.TextField(blank=True, null=True)
    race = models.TextField(blank=True, null=True)
    sex = models.TextField(blank=True, null=True)
    capital_gain = models.IntegerField(blank=True, null=True)
    capital_loss = models.IntegerField(blank=True, null=True)
    hours_per_week = models.IntegerField(blank=True, null=True)
    native_country = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table='Adult'