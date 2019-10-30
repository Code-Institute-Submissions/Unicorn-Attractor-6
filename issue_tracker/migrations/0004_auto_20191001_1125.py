# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-10-01 11:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('issue_tracker', '0003_auto_20190928_1114'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='bug',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='user',
        ),
        migrations.RemoveField(
            model_name='bug',
            name='comments_count',
        ),
        migrations.RemoveField(
            model_name='bug',
            name='is_urgent',
        ),
        migrations.RemoveField(
            model_name='bug',
            name='number_of_likes',
        ),
        migrations.RemoveField(
            model_name='bug',
            name='published_date',
        ),
        migrations.RemoveField(
            model_name='bug',
            name='repair_status',
        ),
        migrations.RemoveField(
            model_name='bug',
            name='votes',
        ),
        migrations.AddField(
            model_name='bug',
            name='status',
            field=models.CharField(choices=[('todo', 'TODO'), ('doing', 'DOING'), ('done', 'DONE')], default='to do', max_length=6),
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
    ]