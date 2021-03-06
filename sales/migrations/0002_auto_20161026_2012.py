# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-26 18:12
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('exhibitors', '0003_exhibitor_location'),
        ('fair', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sales', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Campaign',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Sales',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('not_contacted', 'Not contacted'), ('unreachable', 'Unreachable'), ('not_interested', 'Not interested'), ('contacted', 'Contacted'), ('interested', 'Interested'), ('will_register', 'Will register'), ('registered', 'Registered'), ('fa_contacted', 'FA contacted'), ('fa_on_the_go', 'FA on the go'), ('pending_ad_approval', 'Pending ad approval'), ('ad_sent_for_approval', 'Ad sent for approval'), ('ad_wrong', 'Ad wrong'), ('completed', 'Completed'), ('rejected', 'Rejected')], default='not_contacted', max_length=30, null=True)),
                ('follow_up', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
                ('campaign', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sales.Campaign')),
                ('exhibitor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exhibitors.Exhibitor')),
                ('responsible', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SalesPeriod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('fair', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fair.Fair')),
            ],
        ),
        migrations.RemoveField(
            model_name='sale',
            name='company',
        ),
        migrations.RemoveField(
            model_name='sale',
            name='fair',
        ),
        migrations.RemoveField(
            model_name='sale',
            name='responsible',
        ),
        migrations.DeleteModel(
            name='Sale',
        ),
        migrations.AddField(
            model_name='campaign',
            name='sales_period',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sales.SalesPeriod'),
        ),
    ]
