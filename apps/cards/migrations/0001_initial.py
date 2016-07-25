# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-25 20:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CreditCards',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_name', models.CharField(max_length=40)),
                ('cash_withdrawal_limit', models.PositiveIntegerField()),
                ('swipe_shopping_limit', models.PositiveIntegerField()),
                ('online_shopping_limit', models.PositiveIntegerField()),
                ('reward_points', models.PositiveSmallIntegerField()),
                ('pusrchase_protection', models.PositiveIntegerField()),
                ('insurance_air', models.PositiveIntegerField()),
                ('insurance_non_air', models.PositiveIntegerField()),
                ('fuel_surcharge_waiver', models.BooleanField(default=False)),
                ('emv_chip', models.BooleanField(default=False)),
                ('bookmyshow', models.BooleanField(default=False)),
                ('big_cinemas', models.BooleanField(default=False)),
                ('airport_lounge_access', models.PositiveIntegerField()),
                ('joining_fee', models.PositiveIntegerField()),
                ('annual_fee', models.PositiveIntegerField()),
            ],
        ),
    ]
