# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-31 21:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0020_auto_20161031_2226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='capacity',
            field=models.PositiveSmallIntegerField(blank=True, default=0),
        ),
    ]
