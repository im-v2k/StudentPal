# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-08 22:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('performance', '0004_auto_20171009_0344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exam',
            name='course',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='performance.Course'),
        ),
    ]