# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-30 19:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matching', '0007_auto_20170630_1957'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booleanans',
            name='ans',
            field=models.BooleanField(choices=[(True, 'yes'), (False, 'no')]),
        ),
        migrations.AlterField(
            model_name='question',
            name='name',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
    ]
