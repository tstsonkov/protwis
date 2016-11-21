# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-26 07:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ligand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('canonical', models.NullBooleanField()),
                ('ambigious_alias', models.NullBooleanField()),
            ],
            options={
                'db_table': 'ligand',
            },
        ),
        migrations.CreateModel(
            name='LigandProperities',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('smiles', models.TextField(null=True)),
                ('inchikey', models.CharField(max_length=50, null=True, unique=True)),
            ],
            options={
                'db_table': 'ligand_properities',
            },
        ),
        migrations.CreateModel(
            name='LigandRole',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(unique=True)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'ligand_role',
            },
        ),
        migrations.CreateModel(
            name='LigandType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=20, unique=True)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'ligand_type',
            },
        ),
        migrations.AddField(
            model_name='ligandproperities',
            name='ligand_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ligand.LigandType'),
        ),
        migrations.AddField(
            model_name='ligandproperities',
            name='web_links',
            field=models.ManyToManyField(to='common.WebLink'),
        ),
        migrations.AddField(
            model_name='ligand',
            name='properities',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ligand.LigandProperities'),
        ),
        migrations.AlterUniqueTogether(
            name='ligand',
            unique_together=set([('name', 'canonical')]),
        ),
    ]
