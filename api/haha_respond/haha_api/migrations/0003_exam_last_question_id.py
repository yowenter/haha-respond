# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-01-19 02:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('haha_api', '0002_auto_20180116_1222'),
    ]

    operations = [
        migrations.AddField(
            model_name='exam',
            name='last_question_id',
            field=models.CharField(blank=True, max_length=64),
        ),
    ]
