# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-02-18 21:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fair', '0002_partner_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fair',
            name='name',
            field=models.CharField(default='Armada 2017', max_length=100),
        ),
        migrations.AlterField(
            model_name='fair',
            name='year',
            field=models.IntegerField(default=2017),
        ),
    ]