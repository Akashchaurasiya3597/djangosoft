# Generated by Django 3.0 on 2020-02-17 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ModelFormApp', '0002_customer_model_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer_model',
            name='pic',
            field=models.ImageField(blank=True, max_length=10, upload_to='content/'),
        ),
    ]
