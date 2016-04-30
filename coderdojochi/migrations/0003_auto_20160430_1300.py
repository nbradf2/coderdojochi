# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-30 13:00
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coderdojochi', '0002_auto_20160109_1801'),
    ]

    operations = [
        migrations.CreateModel(
            name='RaceEthnicity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('race_ethnicity', models.CharField(max_length=255)),
                ('visible', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'race and ethnicity',
                'verbose_name_plural': 'races and ethnicities',
            },
        ),
        migrations.AddField(
            model_name='student',
            name='school_name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='school_type',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='session',
            name='end_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 5, 1, 13, 0)),
        ),
        migrations.AlterField(
            model_name='session',
            name='mentor_end_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 5, 1, 14, 0)),
        ),
        migrations.AlterField(
            model_name='session',
            name='mentor_start_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 5, 1, 9, 0)),
        ),
        migrations.AlterField(
            model_name='session',
            name='start_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 5, 1, 10, 0)),
        ),
        migrations.AddField(
            model_name='student',
            name='race_ethnicity',
            field=models.ManyToManyField(null=True, to='coderdojochi.RaceEthnicity'),
        ),
    ]
