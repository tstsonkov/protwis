# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-25 10:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('construct', '0007_auto_20161024_1407'),
    ]

    operations = [
        migrations.AddField(
            model_name='constructmutation',
            name='mutation_type',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='crystallization',
            name='protein_conc',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='crystallization',
            name='temp',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='crystallizationligandconc',
            name='ligand_conc',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
