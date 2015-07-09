# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='VisualBooking',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('total_value', models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)),
                ('search_result_id', models.IntegerField()),
            ],
            options={
                'db_table': 'visual_booking',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='VisualCity',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=30, null=True, blank=True)),
                ('a_name', models.CharField(max_length=20, null=True, blank=True)),
            ],
            options={
                'db_table': 'visual_city',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='VisualCompetitiveOta',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('price', models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)),
                ('percent_diff', models.IntegerField(null=True, blank=True)),
                ('availablity', models.NullBooleanField()),
                ('high_low_same', models.CharField(max_length=1, null=True, blank=True)),
            ],
            options={
                'db_table': 'visual_competitive_ota',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='VisualCountry',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=40, null=True, blank=True)),
                ('a_name', models.CharField(max_length=20, null=True, blank=True)),
            ],
            options={
                'db_table': 'visual_country',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='VisualDateInfo',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('date_time', models.DateTimeField()),
                ('length_of_stay', models.IntegerField()),
                ('booking_window', models.IntegerField()),
                ('arrive', models.DateField(null=True, blank=True)),
                ('leave', models.DateField(null=True, blank=True)),
            ],
            options={
                'db_table': 'visual_date_info',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='VisualHotel',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=30, null=True, blank=True)),
                ('a_name', models.CharField(max_length=20, null=True, blank=True)),
                ('star_rating', models.IntegerField(null=True, blank=True)),
                ('independent', models.NullBooleanField()),
                ('desirability', models.DecimalField(max_digits=10, decimal_places=5, null=True, blank=True)),
                ('country', models.ForeignKey(to='visual.VisualCountry', blank=True, null=True)),
            ],
            options={
                'db_table': 'visual_hotel',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='VisualSearch',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('no_adults', models.IntegerField()),
                ('no_children', models.IntegerField()),
                ('no_rooms', models.IntegerField()),
                ('dest_city', models.ForeignKey(to='visual.VisualCity')),
            ],
            options={
                'db_table': 'visual_search',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='VisualSearchResult',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('rank_pos', models.IntegerField()),
                ('price', models.DecimalField(max_digits=10, decimal_places=2)),
                ('promo_flag', models.BooleanField()),
                ('affinity_score', models.DecimalField(max_digits=65535, decimal_places=65535, null=True, blank=True)),
                ('if_clicked', models.BooleanField()),
                ('short_stay_sat', models.BooleanField()),
                ('prop_review_score', models.DecimalField(max_digits=65535, decimal_places=65535, null=True, blank=True)),
                ('random_bool', models.BooleanField()),
                ('hotel_id', models.IntegerField()),
                ('search_id', models.IntegerField()),
                ('booking_bool', models.NullBooleanField()),
                ('total_price', models.DecimalField(max_digits=65535, decimal_places=65535, null=True, blank=True)),
                ('hist_price', models.DecimalField(max_digits=65535, decimal_places=65535, null=True, blank=True)),
            ],
            options={
                'db_table': 'visual_search_result',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='VisualSite',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=30, null=True, blank=True)),
                ('a_name', models.CharField(max_length=20, null=True, blank=True)),
            ],
            options={
                'db_table': 'visual_site',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='VisualVisitor',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('dist_to_dest', models.DecimalField(max_digits=65535, decimal_places=65535, null=True, blank=True)),
                ('mean_star_rating', models.DecimalField(max_digits=65535, decimal_places=65535, null=True, blank=True)),
                ('mean_price', models.DecimalField(max_digits=65535, decimal_places=65535, null=True, blank=True)),
                ('country', models.ForeignKey(to='visual.VisualCountry')),
                ('search', models.ForeignKey(to='visual.VisualSearch')),
            ],
            options={
                'db_table': 'visual_visitor',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='visualsearchresult',
            name='site',
            field=models.ForeignKey(to='visual.VisualSite', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='visualdateinfo',
            name='search',
            field=models.ForeignKey(to='visual.VisualSearch', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='visualcity',
            name='country',
            field=models.ForeignKey(to='visual.VisualCountry', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='visualbooking',
            name='site',
            field=models.ForeignKey(to='visual.VisualSite'),
        ),
    ]
