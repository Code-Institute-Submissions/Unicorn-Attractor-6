# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-10-07 11:06
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('issue_tracker', '0005_auto_20191007_1051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bug',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
