# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-06-05 14:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dictionary', '0041_auto_20180418_1218'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dataset',
            old_name='description',
            new_name='public_name',
        ),
    ]
