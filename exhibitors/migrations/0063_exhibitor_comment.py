# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-10-19 13:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exhibitors', '0062_auto_20171012_1910'),
    ]

    operations = [
        migrations.AddField(
            model_name='exhibitor',
            name='comment',
            field=models.TextField(blank=True),
        ),
    ]
