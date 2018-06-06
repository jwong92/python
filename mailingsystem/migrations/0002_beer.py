# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-05 16:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailingsystem', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Beer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('temperature', models.FloatField(default=0)),
                ('rec_date', models.DateTimeField(verbose_name='date recorded')),
            ],
        ),
    ]
