# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-30 13:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('compounds', '0002_compound_bfp'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChEMBL',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chembl_id', models.CharField(blank=True, max_length=1024, null=True, verbose_name='ChEMBL ID')),
                ('compound', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='chembl', to='compounds.Compound')),
            ],
            options={
                'verbose_name_plural': 'ChEMBL ID',
            },
        ),
        migrations.CreateModel(
            name='ChEMBL_info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('canonical_smi', models.CharField(blank=True, max_length=1024, null=True)),
                ('max_phase', models.SmallIntegerField(blank=True, null=True)),
                ('prodrug', models.SmallIntegerField(blank=True, null=True)),
                ('oral', models.SmallIntegerField(blank=True, null=True)),
                ('pref_name', models.CharField(blank=True, max_length=1024, null=True)),
                ('activity_id', models.IntegerField(blank=True, null=True)),
                ('assay_id', models.IntegerField(blank=True, null=True)),
                ('tanimoto', models.FloatField(blank=True, null=True)),
                ('chembl_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='chembl_info', to='compounds.ChEMBL')),
            ],
        ),
    ]
