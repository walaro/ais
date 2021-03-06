# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-30 15:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matching', '0030_merge_20171027_1420'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='studentanswerbase',
            options={'default_permissions': (), 'verbose_name': 'answers base'},
        ),
        migrations.AlterModelOptions(
            name='studentanswergrading',
            options={'default_permissions': (), 'verbose_name': 'answer grading', 'verbose_name_plural': 'answers grading'},
        ),
        migrations.AlterModelOptions(
            name='studentanswerslider',
            options={'default_permissions': (), 'verbose_name': 'answer slider', 'verbose_name_plural': 'answers slider'},
        ),
        migrations.AlterModelOptions(
            name='studentanswerworkfield',
            options={'default_permissions': (), 'verbose_name': 'answer workfield', 'verbose_name_plural': 'answers workfield'},
        ),
        migrations.AlterField(
            model_name='studentanswergrading',
            name='answer',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='studentanswerslider',
            name='answer_max',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='studentanswerslider',
            name='answer_min',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='studentanswerworkfield',
            name='answer',
            field=models.BooleanField(choices=[(True, 'yes'), (False, 'no')], default=False),
        ),
        migrations.AlterField(
            model_name='studentquestionslider',
            name='units',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
    ]
