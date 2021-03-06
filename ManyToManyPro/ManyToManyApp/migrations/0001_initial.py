# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2020-01-27 11:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Company_Name', models.CharField(max_length=100)),
                ('Company_Email', models.EmailField(max_length=100)),
                ('Company_Number', models.BigIntegerField()),
                ('Company_Website', models.URLField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='PersonData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_Name', models.CharField(max_length=100)),
                ('Last_Name', models.CharField(max_length=100)),
                ('Age', models.IntegerField()),
                ('Email', models.EmailField(max_length=100)),
                ('Mobile_Number', models.BigIntegerField()),
                ('CompanyDatahere', models.ManyToManyField(null=True, to='ManyToManyApp.CompanyData')),
            ],
        ),
    ]
