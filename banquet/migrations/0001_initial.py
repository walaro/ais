# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-09-26 18:21
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('exhibitors', '0060_auto_20170926_2021'),
        ('fair', '0006_auto_20170831_2211'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]
    state_operations = [
        migrations.CreateModel(
            name='BanquetteAttendant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('linkedin_url', models.URLField(blank=True)),
                ('job_title', models.CharField(blank=True, max_length=200)),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')], max_length=10)),
                ('phone_number', models.CharField(max_length=200)),
                ('allergies', models.CharField(blank=True, max_length=1000)),
                ('student_ticket', models.BooleanField(default=False)),
                ('wants_alcohol', models.BooleanField(default=True)),
                ('wants_lactose_free_food', models.BooleanField(default=False)),
                ('wants_gluten_free_food', models.BooleanField(default=False)),
                ('wants_vegetarian_food', models.BooleanField(default=True)),
                ('table_name', models.CharField(blank=True, max_length=20, null=True)),
                ('seat_number', models.SmallIntegerField(blank=True, null=True)),
                ('ignore_from_placement', models.BooleanField(default=False)),
                ('exhibitor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='exhibitors.Exhibitor')),
                ('fair', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='fair.Fair')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['first_name', 'last_name'],
            },
        ),
    ]
    operations = [
        migrations.SeparateDatabaseAndState(state_operations=state_operations)
    ]
