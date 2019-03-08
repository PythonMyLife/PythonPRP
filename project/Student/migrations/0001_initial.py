# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-10-07 05:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DataModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_ID', models.CharField(max_length=12)),
                ('name', models.CharField(max_length=30)),
                ('department', models.CharField(max_length=20)),
                ('major', models.CharField(max_length=20)),
                ('grade', models.IntegerField()),
                ('graduate_time', models.CharField(max_length=10)),
                ('student_status', models.CharField(max_length=4)),
                ('failed_number', models.IntegerField()),
                ('center_credits', models.IntegerField()),
                ('courses_must_to_take', models.CharField(max_length=400)),
                ('general_courses', models.CharField(max_length=50)),
                ('one_direction', models.CharField(max_length=50)),
                ('another_direction', models.CharField(max_length=50)),
                ('others', models.CharField(max_length=1000)),
            ],
        ),
    ]
