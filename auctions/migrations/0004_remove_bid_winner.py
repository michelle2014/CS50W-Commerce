# Generated by Django 3.0.8 on 2020-09-01 09:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0003_bid_winner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bid',
            name='winner',
        ),
    ]
