# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-09 23:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0006_auto_20160822_1051'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'permissions': (('view_people', 'View people'),)},
        ),
    ]
