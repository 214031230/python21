# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-11-08 07:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('repository', '0005_auto_20181107_1057'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdminInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=32, verbose_name='用户名')),
                ('password', models.CharField(max_length=32, verbose_name='密码')),
            ],
        ),
        migrations.CreateModel(
            name='BusinessUnit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True, verbose_name='业务线名称')),
            ],
            options={
                'verbose_name_plural': '业务线表',
            },
        ),
        migrations.CreateModel(
            name='IDC',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='机房')),
                ('floor', models.IntegerField(default=1, verbose_name='楼层')),
            ],
            options={
                'verbose_name_plural': '机房表',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, unique=True, verbose_name='标签')),
            ],
            options={
                'verbose_name_plural': '标签表',
            },
        ),
        migrations.CreateModel(
            name='UserGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, unique=True, verbose_name='用户组名称')),
            ],
            options={
                'verbose_name_plural': '用户组表',
            },
        ),
        migrations.AddField(
            model_name='server',
            name='cabinet_num',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='机柜号'),
        ),
        migrations.AddField(
            model_name='server',
            name='cabinet_order',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='机柜中序号'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='邮箱地址'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='mobile',
            field=models.CharField(max_length=32, verbose_name='手机号'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='phone',
            field=models.CharField(max_length=32, verbose_name='座机号'),
        ),
        migrations.AddField(
            model_name='usergroup',
            name='users',
            field=models.ManyToManyField(to='repository.UserProfile', verbose_name='关联用户'),
        ),
        migrations.AddField(
            model_name='businessunit',
            name='contact',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='c', to='repository.UserGroup', verbose_name='所属业务线组'),
        ),
        migrations.AddField(
            model_name='businessunit',
            name='manager',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='m', to='repository.UserGroup', verbose_name='所属运维管理'),
        ),
        migrations.AddField(
            model_name='admininfo',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='repository.UserProfile', verbose_name='关联用户'),
        ),
        migrations.AddField(
            model_name='server',
            name='business_unit',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='repository.BusinessUnit'),
        ),
        migrations.AddField(
            model_name='server',
            name='idc',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='repository.IDC'),
        ),
        migrations.AddField(
            model_name='server',
            name='tags',
            field=models.ManyToManyField(to='repository.Tag'),
        ),
    ]
