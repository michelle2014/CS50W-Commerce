# Generated by Django 3.0.8 on 2020-09-03 02:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0007_auto_20200902_2317'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='image_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
