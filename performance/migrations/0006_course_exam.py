# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-26 00:19
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('performance', '0005_auto_20171026_0548'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(default='', max_length=20)),
                ('name', models.CharField(default='', max_length=50)),
                ('teacher', models.CharField(default='', max_length=50)),
                ('comment', models.TextField(default='')),
                ('sem', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('weightage', models.PositiveSmallIntegerField(default=100)),
                ('max_marks', models.PositiveSmallIntegerField(default=100)),
                ('marks_obt', models.PositiveSmallIntegerField(default=0)),
                ('comment', models.TextField(blank=True, default='')),
                ('course', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='performance.Course')),
            ],
        ),
    ]