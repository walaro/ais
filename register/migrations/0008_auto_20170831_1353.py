# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-08-31 11:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0007_orderlog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderlog',
            name='timestamp',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
