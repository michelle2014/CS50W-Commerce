# Generated by Django 3.0.8 on 2020-09-01 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0002_listing_winner'),
    ]

    operations = [
        migrations.AddField(
            model_name='bid',
            name='winner',
            field=models.BooleanField(default=False),
        ),
    ]