# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-11 21:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0012_company_organisation_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='additional_address_information',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]