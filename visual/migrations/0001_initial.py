# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('total_value', models.DecimalField(max_digits=10, decimal_places=2, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('a_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Competitive_OTA',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('price', models.DecimalField(max_digits=10, decimal_places=2, null=True)),
                ('percent_diff', models.IntegerField(null=True)),
                ('availablity', models.NullBooleanField()),
                ('high_low_same', models.CharField(max_length=1, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('a_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Date_Info',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('date_time', models.DateTimeField(default='2013-04-04 08:32:15')),
                ('length_of_stay', models.IntegerField(default=0)),
                ('booking_window', models.IntegerField(default=0)),
                ('arrival', models.DateField(null=True)),
                ('checkOut', models.DateField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=30, default='default')),
                ('a_name', models.CharField(max_length=20, default='default')),
                ('star_rating', models.IntegerField(default=0)),
                ('independent', models.BooleanField(default=0)),
                ('desirability', models.DecimalField(max_digits=10, decimal_places=5, null=True)),
                ('hist_price', models.DecimalField(max_digits=10, decimal_places=2, null=True)),
                ('country', models.ForeignKey(to='visual.Country', default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Search',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('no_adults', models.IntegerField(default=1)),
                ('no_children', models.IntegerField(default=0)),
                ('no_rooms', models.IntegerField(default=1)),
                ('date_info', models.ForeignKey(to='visual.Date_Info', default=0)),
                ('dest_city', models.ForeignKey(to='visual.City', default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Search_Result',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('rank_pos', models.IntegerField(default=0)),
                ('price', models.DecimalField(max_digits=10, decimal_places=2)),
                ('promo_flag', models.BooleanField(default=0)),
                ('affinity_score', models.DecimalField(max_digits=10, decimal_places=5, null=True)),
                ('if_clicked', models.BooleanField(default=0)),
                ('short_stay_sat', models.BooleanField(default=0)),
                ('prop_review_score', models.DecimalField(max_digits=2, decimal_places=2, null=True)),
                ('random_bool', models.BooleanField(default=0)),
                ('hotel', models.ForeignKey(to='visual.Hotel', default=0)),
                ('search', models.ForeignKey(to='visual.Search', default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('a_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Visitor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('dist_to_dest', models.IntegerField(default=0)),
                ('mean_star_rating', models.DecimalField(max_digits=2, decimal_places=2, null=True)),
                ('mean_price', models.DecimalField(max_digits=10, decimal_places=2, null=True)),
                ('country', models.ForeignKey(to='visual.Country', default=0)),
                ('search_result', models.ForeignKey(to='visual.Search_Result', default=0)),
            ],
        ),
        migrations.AddField(
            model_name='competitive_ota',
            name='search_result',
            field=models.ForeignKey(to='visual.Search_Result'),
        ),
        migrations.AddField(
            model_name='city',
            name='country_id',
            field=models.ForeignKey(to='visual.Country', default=0),
        ),
        migrations.AddField(
            model_name='booking',
            name='search_result',
            field=models.ForeignKey(to='visual.Search_Result', default=0),
        ),
        migrations.AddField(
            model_name='booking',
            name='site',
            field=models.ForeignKey(to='visual.Site', default=0),
        ),
    ]
