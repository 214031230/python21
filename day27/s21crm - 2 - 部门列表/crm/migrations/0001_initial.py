# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-11-11 01:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('rbac', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32, verbose_name='部门')),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=32, verbose_name='用户名')),
                ('password', models.CharField(max_length=64, verbose_name='密码')),
                ('email', models.EmailField(max_length=254, verbose_name='邮箱')),
                ('phone', models.CharField(max_length=32, verbose_name='手机')),
                ('depart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.Department', verbose_name='部门')),
                ('roles', models.ManyToManyField(to='rbac.Role', verbose_name='关联角色')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
