# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-02 19:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0009_event_attendence_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='description_short',
            field=models.TextField(blank=True),
        ),
    ]
