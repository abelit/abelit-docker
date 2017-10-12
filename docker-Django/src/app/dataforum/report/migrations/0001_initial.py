# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-08-30 03:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OracleServer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_name', models.CharField(max_length=50)),
                ('db_user', models.CharField(max_length=50)),
                ('db_password', models.CharField(max_length=50)),
                ('db_port', models.IntegerField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Server',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('server_name', models.CharField(max_length=50)),
                ('ipaddress', models.CharField(max_length=45)),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('ssh_port', models.IntegerField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='ServerMetric',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hostname', models.CharField(max_length=45)),
                ('cpu', models.CharField(max_length=45)),
                ('memory', models.CharField(max_length=45)),
                ('disk', models.CharField(max_length=45)),
                ('system', models.CharField(max_length=45)),
                ('datetime', models.DateTimeField()),
                ('cpu_load', models.CharField(max_length=45)),
                ('disk_usage', models.CharField(max_length=45)),
                ('memory_usage', models.CharField(max_length=45)),
                ('server', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='report.Server')),
            ],
        ),
        migrations.AddField(
            model_name='oracleserver',
            name='server',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='report.Server'),
        ),
    ]