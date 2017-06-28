# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-30 11:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exhibitors', '0050_auto_20170526_1807'),
    ]

    operations = [
        migrations.AddField(
            model_name='exhibitor',
            name='requests_for_exhibition_area',
            field=models.CharField(blank=True, choices=[('kth_library', 'KTH Library'), ('kth_entre', 'KTH Entré'), ('nymble', 'Nymble')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='exhibitor',
            name='requests_for_stand_placement',
            field=models.CharField(blank=True, choices=[('mixed', 'Mixed with a diverse group of companies'), ('same_industry', 'In connection with companies in the same industry/field')], max_length=200, null=True),
        ),
    ]