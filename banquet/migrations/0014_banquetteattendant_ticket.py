# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-10-11 18:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('banquet', '0011_auto_20171010_2205'),
    ]

    operations = [
        migrations.AddField(
            model_name='banquetteattendant',
            name='ticket',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='banquet.BanquetTicket'),
        ),
    ]
