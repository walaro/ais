# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-01 23:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('matching', '0033_auto_20171101_1239'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_type', models.TextField()),
                ('job_type_id', models.IntegerField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='StudentAnswerJobType',
            fields=[
                ('studentanswerbase_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='matching.StudentAnswerBase')),
                ('job_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='matching.JobType')),
            ],
            options={
                'verbose_name': 'answer job type',
            },
            bases=('matching.studentanswerbase',),
        ),
    ]
