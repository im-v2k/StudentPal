# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-20 11:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('performance', '0011_auto_20171020_1650'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exam',
            name='name',
            field=models.CharField(max_length=30),
        ),
    ]
