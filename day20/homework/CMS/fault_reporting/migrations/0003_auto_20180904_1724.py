# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-04 09:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fault_reporting', '0002_auto_20180904_1721'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='parent_comment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='fault_reporting.Comment', verbose_name='父级评论'),
        ),
    ]
