# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-25 18:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exhibitors', '0047_banquetteattendant_fair'),
    ]

    operations = [
        migrations.AddField(
            model_name='exhibitor',
            name='number_of_outlets_needed',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='exhibitor',
            name='total_power',
            field=models.CharField(blank=True, max_length=500),
        ),
    ]
