# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-01 19:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recruitment', '0026_auto_20160919_1036'),
        ('events', '0022_auto_20161031_2330'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='extra_field',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='recruitment.ExtraField'),
        ),
    ]
