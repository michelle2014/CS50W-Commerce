# Generated by Django 3.0.8 on 2020-09-03 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0008_listing_image_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='bid_count',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=3, null=True),
        ),
    ]
