# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-11-09 12:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0004_followup_sale'),
    ]

    operations = [
        migrations.AlterField(
            model_name='followup',
            name='sale',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sales.Sale'),
        ),
    ]
