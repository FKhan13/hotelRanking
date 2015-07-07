# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('visual', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompetitiveOta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('price', models.DecimalField(blank=True, null=True, decimal_places=2, max_digits=10)),
                ('percent_diff', models.IntegerField(blank=True, null=True)),
                ('availablity', models.NullBooleanField()),
                ('high_low_same', models.CharField(blank=True, null=True, max_length=1)),
            ],
            options={
                'db_table': 'visual_competitive_ota',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DateInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('date_time', models.DateTimeField()),
                ('length_of_stay', models.IntegerField()),
                ('booking_window', models.IntegerField()),
                ('arrival', models.DateField(blank=True, null=True)),
                ('leave', models.DateField(blank=True, null=True)),
            ],
            options={
                'db_table': 'visual_date_info',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SearchResult',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('rank_pos', models.IntegerField()),
                ('price', models.DecimalField(max_digits=10, decimal_places=2)),
                ('promo_flag', models.BooleanField()),
                ('affinity_score', models.DecimalField(blank=True, null=True, decimal_places=5, max_digits=10)),
                ('if_clicked', models.BooleanField()),
                ('short_stay_sat', models.BooleanField()),
                ('prop_review_score', models.DecimalField(blank=True, null=True, decimal_places=2, max_digits=2)),
                ('random_bool', models.BooleanField()),
            ],
            options={
                'db_table': 'visual_search_result',
                'managed': False,
            },
        ),
        migrations.RemoveField(
            model_name='competitive_ota',
            name='search_result',
        ),
        migrations.DeleteModel(
            name='Date_Info',
        ),
        migrations.RemoveField(
            model_name='search_result',
            name='hotel',
        ),
        migrations.RemoveField(
            model_name='search_result',
            name='search',
        ),
        migrations.AlterModelOptions(
            name='booking',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='city',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='country',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='hotel',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='search',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='site',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='visitor',
            options={'managed': False},
        ),
        migrations.DeleteModel(
            name='Competitive_OTA',
        ),
        migrations.DeleteModel(
            name='Search_Result',
        ),
    ]
