# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-11-06 10:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matching', '0041_merge_20171106_1145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='continent',
            name='survey',
            field=models.ManyToManyField(to='matching.Survey'),
        ),
        migrations.AlterField(
            model_name='swedenregion',
            name='survey',
            field=models.ManyToManyField(to='matching.Survey'),
        ),
    ]