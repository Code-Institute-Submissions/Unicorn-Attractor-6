# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-11-14 01:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('issue_tracker', '0009_auto_20191113_2348'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bug',
            name='votes',
        ),
        migrations.AddField(
            model_name='bug',
            name='votes',
            field=models.IntegerField(default=0),
        ),
    ]