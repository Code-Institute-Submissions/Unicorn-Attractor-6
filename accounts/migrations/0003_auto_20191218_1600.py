# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2019-12-18 16:00
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20191216_1118'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='user_p',
            new_name='user',
        ),
    ]