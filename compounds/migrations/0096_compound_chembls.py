# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-02 11:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compounds', '0095_chembl'),
    ]

    operations = [
        migrations.AddField(
            model_name='compound',
            name='chembls',
            field=models.ManyToManyField(blank=True, to='compounds.ChEMBL'),
        ),
    ]
