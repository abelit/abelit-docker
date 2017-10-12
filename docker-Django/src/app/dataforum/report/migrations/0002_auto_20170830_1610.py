# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-08-30 08:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Host',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('ipaddress', models.CharField(max_length=20)),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=20)),
                ('ssh_port', models.IntegerField()),
                ('hostname', models.CharField(blank=True, max_length=45)),
                ('cpu', models.CharField(blank=True, max_length=45)),
                ('memory', models.CharField(blank=True, max_length=45)),
                ('disk', models.CharField(blank=True, max_length=45)),
                ('system', models.CharField(blank=True, max_length=45)),
                ('application', models.CharField(blank=True, max_length=100)),
                ('remark', models.TextField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='HostMetric',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cpu_load', models.CharField(max_length=45)),
                ('disk_usage', models.CharField(max_length=45)),
                ('memory_usage', models.CharField(max_length=45)),
                ('datetime', models.DateTimeField()),
                ('host', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='report.Host')),
            ],
        ),
        migrations.CreateModel(
            name='Oracle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('db_user', models.CharField(max_length=50)),
                ('db_password', models.CharField(max_length=20)),
                ('db_port', models.IntegerField(max_length=8)),
                ('db_id', models.CharField(blank=True, max_length=20)),
                ('db_name', models.CharField(blank=True, max_length=30)),
                ('db_version', models.CharField(blank=True, max_length=20)),
                ('service_name', models.CharField(blank=True, max_length=20)),
                ('remark', models.TextField(blank=True, max_length=100)),
                ('host', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='report.Host')),
            ],
        ),
        migrations.RemoveField(
            model_name='oracleserver',
            name='server',
        ),
        migrations.RemoveField(
            model_name='servermetric',
            name='server',
        ),
        migrations.DeleteModel(
            name='OracleServer',
        ),
        migrations.DeleteModel(
            name='Server',
        ),
        migrations.DeleteModel(
            name='ServerMetric',
        ),
    ]