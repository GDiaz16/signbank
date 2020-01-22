# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-20 10:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dictionary', '0031_auto_20170920_1051'),
    ]

    operations = [
        migrations.RenameField('gloss', 'locked', 'published'),
        migrations.AlterModelOptions(
            name='gloss',
            options={'ordering': ['idgloss'], 'permissions': (
            ('update_video', 'Can Update Video'), ('search_gloss', 'Can Search/View Full Gloss Details'),
            ('export_csv', 'Can export sign details as CSV'), ('import_csv', 'Can import glosses from a CSV file'),
            ('can_publish', 'Can publish signs and definitions'),
            ('view_advanced_properties', 'Include all properties in sign detail view'),
            ('publish_gloss', 'Can publish and unpublish Glosses')), 'verbose_name_plural': 'Glosses'},
        ),
        migrations.AlterField(
            model_name='gloss',
            name='published',
            field=models.BooleanField(default=False, verbose_name='Published'),
        ),
    ]
