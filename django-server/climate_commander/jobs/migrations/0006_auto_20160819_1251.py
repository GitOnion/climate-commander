# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-19 19:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0005_server_job_running'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobRunningOnServer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField(verbose_name='Time When the Job Starts')),
                ('status', models.CharField(max_length=6000, null=True)),
                ('pid', models.CharField(max_length=2000)),
            ],
        ),
        migrations.RemoveField(
            model_name='job',
            name='pid',
        ),
        migrations.RemoveField(
            model_name='job',
            name='run_time',
        ),
        migrations.RemoveField(
            model_name='job',
            name='status',
        ),
        migrations.RemoveField(
            model_name='server',
            name='job_running',
        ),
        migrations.AddField(
            model_name='jobrunningonserver',
            name='job',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobs.Job'),
        ),
        migrations.AddField(
            model_name='jobrunningonserver',
            name='server',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobs.Server'),
        ),
        migrations.AddField(
            model_name='job',
            name='server_running',
            field=models.ManyToManyField(through='jobs.JobRunningOnServer', to='jobs.Server'),
        ),
    ]
