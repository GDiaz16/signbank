# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-10-24 20:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dictionary', '0047_auto_20180629_1415'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gloss',
            name='location',
            field=models.ForeignKey(blank=True, choices=[(-1, 'No Value Set'), (0, 'N/A'), (1, 'Top of head'), (2, 'Forehead'), (3, 'Temple'), (4, 'Eye'), (5, 'Nose'), (6, 'Whole of face'), (7, 'Cheekbone'), (8, 'Ear or side of head'), (9, 'Cheek'), (10, 'Mouth and lips'), (11, 'Chin'), (12, 'Neck'), (13, 'Shoulder'), (14, 'Chest'), (28, 'High neutral space'), (15, 'Stomach'), (29, 'Neutral space'), (16, 'Waist'), (17, 'Below waist'), (18, 'Upper arm'), (19, 'Elbow'), (20, 'Pronated forearm'), (21, 'Supinated forearm'), (22, 'Pronated wrist'), (23, 'Spinated wrist'), (24, 'Back of hand'), (25, 'Palm'), (26, 'Edge of hand'), (27, 'Fingertips')], db_column='location', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='location', to='dictionary.FieldChoice', to_field='machine_value', verbose_name='Location'),
        ),
    ]