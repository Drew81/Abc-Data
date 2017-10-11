# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-15 14:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('math_score', models.IntegerField()),
                ('reading_score', models.IntegerField()),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='students.Student')),
            ],
        ),
    ]
