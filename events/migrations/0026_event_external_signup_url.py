# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-09 23:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0025_eventattendence_submission_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='external_signup_url',
            field=models.CharField(blank=True, max_length=80),
        ),
    ]
