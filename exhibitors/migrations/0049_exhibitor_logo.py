# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-26 16:01
from __future__ import unicode_literals

from django.db import migrations, models
import lib.image


class Migration(migrations.Migration):

    dependencies = [
        ('exhibitors', '0048_auto_20170525_2050'),
    ]

    operations = [
        migrations.AddField(
            model_name='exhibitor',
            name='logo',
            field=models.ImageField(blank=True, upload_to=lib.image.UploadToDirUUID('exhibitors', 'logo_original')),
        ),
    ]
