# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-11-04 14:26
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('student_profiles', '0007_auto_20171103_1346'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentprofile',
            name='id',
            field=models.AutoField(auto_created=True, default=0, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='studentprofile',
            name='id_string',
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
        ),
    ]
