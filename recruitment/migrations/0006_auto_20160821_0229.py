# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-21 02:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recruitment', '0005_auto_20160821_0000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='role',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
