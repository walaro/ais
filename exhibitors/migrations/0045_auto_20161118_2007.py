# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-18 19:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exhibitors', '0044_auto_20161115_1038'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='exhibitor',
            options={'permissions': (('view_exhibitors', 'View exhibitors'),)},
        ),
    ]
