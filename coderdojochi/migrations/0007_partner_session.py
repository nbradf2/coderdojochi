# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-09-20 17:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coderdojochi', '0006_session_gender_limitation'),
    ]

    operations = [
        migrations.AddField(
            model_name='session',
            name='partner_message',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='session',
            name='password',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
