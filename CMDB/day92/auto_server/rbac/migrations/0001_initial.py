# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-11-13 08:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32, verbose_name='标题')),
                ('icon', models.CharField(max_length=32, verbose_name='图标')),
            ],
            options={
                'verbose_name_plural': '菜单表',
            },
        ),
        migrations.CreateModel(
            name='Permission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=128, verbose_name='URL(含正则)')),
                ('title', models.CharField(max_length=32, verbose_name='名称')),
                ('name', models.CharField(max_length=32, unique=True, verbose_name='别名')),
                ('menu', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='rbac.Menu', verbose_name='管理菜单')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='rbac.Permission', verbose_name='父菜单')),
            ],
            options={
                'verbose_name_plural': '权限表',
            },
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32, verbose_name='名称')),
                ('permissions', models.ManyToManyField(to='rbac.Permission', verbose_name='关联权限')),
            ],
            options={
                'verbose_name_plural': '角色表',
            },
        ),
    ]
