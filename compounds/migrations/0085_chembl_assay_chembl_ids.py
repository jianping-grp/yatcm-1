# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-02 06:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compounds', '0084_auto_20171102_0513'),
    ]

    operations = [
        migrations.AddField(
            model_name='chembl',
            name='assay_chembl_ids',
            field=models.ManyToManyField(blank=True, to='compounds.Assay_Chembl_id'),
        ),
    ]
