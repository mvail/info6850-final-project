# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-04-11 23:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Keywords',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=1000)),
                ('word_count', models.PositiveIntegerField()),
                ('week', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Patent',
            fields=[
                ('pid', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('ptext', models.CharField(max_length=2100000000)),
                ('uspc', models.PositiveIntegerField()),
                ('claims', models.PositiveIntegerField()),
                ('inventors', models.PositiveIntegerField()),
                ('week', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Uspc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('week', models.PositiveIntegerField()),
                ('uspc', models.PositiveIntegerField()),
                ('patent_count', models.PositiveIntegerField()),
            ],
        ),
    ]
