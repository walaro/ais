# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-09 22:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
        ('recruitment', '0018_auto_20160904_0056'),
    ]

    operations = [
        migrations.AddField(
            model_name='role',
            name='group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='auth.Group'),
            preserve_default=False,
        ),
    ]
