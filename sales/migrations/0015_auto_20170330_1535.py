# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-30 13:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0014_auto_20170323_0853'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sale',
            name='diversity_room',
            field=models.BooleanField(default=True),
        ),
    ]
