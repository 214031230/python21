# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-08-06 07:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20180806_1421'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='password',
            field=models.CharField(default='0192023a7bbd73250516f069df18b500', max_length=64),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='username',
            field=models.CharField(max_length=16, unique=True),
        ),
    ]