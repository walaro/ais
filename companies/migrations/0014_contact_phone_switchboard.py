# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-11 23:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0013_company_additional_address_information'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='phone_switchboard',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
