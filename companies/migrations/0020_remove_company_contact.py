# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-04 14:53
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0019_move_company_contact'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='contact',
        ),
    ]