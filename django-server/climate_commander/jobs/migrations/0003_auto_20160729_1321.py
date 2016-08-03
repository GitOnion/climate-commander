# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-29 20:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_job'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='code_url',
            field=models.URLField(default='default_url'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='job',
            name='command',
            field=models.TextField(default='python -m generate.montecarlo /shares/gcp/outputs/nasmort-fireant'),
            preserve_default=False,
        ),
    ]