# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-09-17 19:54
from __future__ import unicode_literals

from django.db import migrations, models
import lib.image


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0008_auto_20161019_1130'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='portrait',
            field=models.ImageField(blank=True, upload_to=lib.image.UploadToDir('profiles', 'portrait')),
        ),
    ]
