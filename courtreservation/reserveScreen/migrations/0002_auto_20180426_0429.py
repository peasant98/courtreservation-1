# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-26 04:29
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reserveScreen', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='court',
            old_name='courtReserved',
            new_name='courtreserved',
        ),
    ]
