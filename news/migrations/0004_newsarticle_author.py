# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-16 21:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_auto_20170510_1039'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsarticle',
            name='author',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
