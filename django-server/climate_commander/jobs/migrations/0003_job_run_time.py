# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-19 05:37
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_remove_job_run_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='run_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 8, 19, 5, 37, 14, 816610, tzinfo=utc), verbose_name='Time of the Last Run'),
            preserve_default=False,
        ),
    ]
