# Generated by Django 3.0 on 2020-02-17 18:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ModelFormApp', '0004_auto_20200217_2327'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer_model',
            name='pic',
        ),
    ]