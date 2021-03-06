# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-01 13:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compounds', '0006_auto_20171001_0800'),
    ]

    operations = [
        migrations.AddField(
            model_name='chembl',
            name='url',
            field=models.URLField(blank=True, max_length=1024, verbose_name='URL link to ChEMBL database'),
        ),
    ]
