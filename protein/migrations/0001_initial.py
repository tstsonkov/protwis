# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-26 07:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gene',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('position', models.SmallIntegerField()),
            ],
            options={
                'ordering': ('position',),
                'db_table': 'gene',
            },
        ),
        migrations.CreateModel(
            name='Protein',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entry_name', models.SlugField(max_length=100, unique=True)),
                ('accession', models.CharField(db_index=True, max_length=100, null=True)),
                ('name', models.CharField(max_length=200)),
                ('sequence', models.TextField()),
            ],
            options={
                'db_table': 'protein',
            },
        ),
        migrations.CreateModel(
            name='ProteinAlias',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('position', models.SmallIntegerField()),
            ],
            options={
                'ordering': ('position',),
                'db_table': 'protein_alias',
            },
        ),
        migrations.CreateModel(
            name='ProteinAnomaly',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'ordering': ('generic_number__label',),
                'db_table': 'protein_anomaly',
            },
        ),
        migrations.CreateModel(
            name='ProteinAnomalyRule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amino_acid', models.CharField(max_length=1)),
                ('negative', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'protein_anomaly_rule',
            },
        ),
        migrations.CreateModel(
            name='ProteinAnomalyRuleSet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exclusive', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ('id',),
                'db_table': 'protein_anomaly_rule_set',
            },
        ),
        migrations.CreateModel(
            name='ProteinAnomalyType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=20, unique=True)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'protein_anomaly_type',
            },
        ),
        migrations.CreateModel(
            name='ProteinConformation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'ordering': ('id',),
                'db_table': 'protein_conformation',
            },
        ),
        migrations.CreateModel(
            name='ProteinConformationTemplateStructure',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('protein_conformation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='protein.ProteinConformation')),
            ],
            options={
                'db_table': 'protein_conformation_template_structure',
            },
        ),
        migrations.CreateModel(
            name='ProteinFamily',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('name', models.CharField(max_length=200)),
                ('parent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='protein.ProteinFamily')),
            ],
            options={
                'ordering': ('id',),
                'db_table': 'protein_family',
            },
        ),
        migrations.CreateModel(
            name='ProteinFusion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('sequence', models.TextField(null=True)),
            ],
            options={
                'db_table': 'protein_fusion',
            },
        ),
        migrations.CreateModel(
            name='ProteinFusionProtein',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('protein', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='protein.Protein')),
                ('protein_fusion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='protein.ProteinFusion')),
            ],
            options={
                'db_table': 'protein_fusion_protein',
            },
        ),
        migrations.CreateModel(
            name='ProteinGProtein',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('sequence', models.TextField(null=True)),
            ],
            options={
                'db_table': 'protein_gprotein',
            },
        ),
        migrations.CreateModel(
            name='ProteinGProteinPair',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transduction', models.TextField(null=True)),
                ('g_protein', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='protein.ProteinGProtein')),
                ('protein', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='protein.Protein')),
            ],
            options={
                'db_table': 'protein_gprotein_pair',
            },
        ),
        migrations.CreateModel(
            name='ProteinSegment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('name', models.CharField(max_length=50)),
                ('category', models.CharField(max_length=50)),
                ('fully_aligned', models.BooleanField(default=False)),
                ('partial', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ('id',),
                'db_table': 'protein_segment',
            },
        ),
        migrations.CreateModel(
            name='ProteinSequenceType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=20, unique=True)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'protein_sequence_type',
            },
        ),
        migrations.CreateModel(
            name='ProteinSet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('proteins', models.ManyToManyField(to='protein.Protein')),
            ],
            options={
                'db_table': 'protein_set',
            },
        ),
        migrations.CreateModel(
            name='ProteinSource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True)),
            ],
            options={
                'db_table': 'protein_source',
            },
        ),
        migrations.CreateModel(
            name='ProteinState',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=20, unique=True)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'protein_state',
            },
        ),
        migrations.CreateModel(
            name='Species',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latin_name', models.CharField(max_length=100, unique=True)),
                ('common_name', models.CharField(blank=True, max_length=100)),
            ],
            options={
                'db_table': 'species',
            },
        ),
        migrations.AddField(
            model_name='proteingprotein',
            name='proteins',
            field=models.ManyToManyField(through='protein.ProteinGProteinPair', to='protein.Protein'),
        ),
        migrations.AddField(
            model_name='proteinfusionprotein',
            name='segment_after',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='segment_after', to='protein.ProteinSegment'),
        ),
        migrations.AddField(
            model_name='proteinfusionprotein',
            name='segment_before',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='segment_before', to='protein.ProteinSegment'),
        ),
        migrations.AddField(
            model_name='proteinfusion',
            name='proteins',
            field=models.ManyToManyField(through='protein.ProteinFusionProtein', to='protein.Protein'),
        ),
        migrations.AddField(
            model_name='proteinconformationtemplatestructure',
            name='protein_segment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='protein.ProteinSegment'),
        ),
    ]
