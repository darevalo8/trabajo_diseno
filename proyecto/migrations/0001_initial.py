# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Companies',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('addres', models.CharField(max_length=100)),
                ('phone', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('start_date', models.DateField(default=datetime.datetime.today)),
                ('end_date', models.DateField()),
                ('salary', models.IntegerField(max_length=20)),
                ('company', models.ForeignKey(to='proyecto.Companies')),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.IntegerField()),
                ('addres', models.CharField(max_length=100)),
                ('profession', models.CharField(max_length=80)),
            ],
        ),
        migrations.AddField(
            model_name='contract',
            name='employee',
            field=models.ForeignKey(to='proyecto.Employee'),
        ),
    ]
