# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-14 17:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0014_event_attendence_approvement_required'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='attendence_approvement_required',
            field=models.BooleanField(default=True, help_text='If this is checked all users that attends the event needs to         be accepted by an admin.'),
        ),
        migrations.AlterField(
            model_name='event',
            name='attendence_description',
            field=models.TextField(blank=True, help_text="This is a text only shown in the attendence form, example         'To be accepted to this event you need to pay the event fee of         500 SEK'"),
        ),
        migrations.AlterField(
            model_name='event',
            name='public_registration',
            field=models.BooleanField(default=False, help_text='If users without an account should be able to sign up for         this event.'),
        ),
        migrations.AlterField(
            model_name='event',
            name='registration_last_day_cancel',
            field=models.DateTimeField(help_text='Last day a user can cancel the attendence to the event', null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='send_submission_mail',
            field=models.BooleanField(default=False, help_text='If checked an email will be sent when a user attends         the event'),
        ),
    ]
