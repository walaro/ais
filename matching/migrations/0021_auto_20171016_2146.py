# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-10-16 19:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matching', '0020_auto_20171016_1610'),
    ]

    operations = [
        migrations.AddField(
            model_name='workfield',
            name='survey',
            field=models.ManyToManyField(to='matching.Survey'),
        ),
        migrations.AlterField(
            model_name='studentquestionbase',
            name='survey',
            field=models.ManyToManyField(blank=True, to='matching.Survey'),
        ),
        migrations.AlterField(
            model_name='workfield',
            name='work_field',
            field=models.TextField(unique=True),
        ),
        migrations.AlterField(
            model_name='workfieldarea',
            name='work_area',
            field=models.TextField(unique=True),
        ),
    ]
