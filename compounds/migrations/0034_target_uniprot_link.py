# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-26 03:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compounds', '0033_compound_tcmid_idx'),
    ]

    operations = [
        migrations.AddField(
            model_name='target',
            name='uniprot_link',
            field=models.URLField(blank=True, max_length=1024, null=True),
        ),
    ]
