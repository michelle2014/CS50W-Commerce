# Generated by Django 3.0.8 on 2020-09-04 02:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0012_remove_listing_watchlist'),
    ]

    operations = [
        migrations.CreateModel(
            name='Watchlist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=255)),
                ('watchlist', models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name='listing',
            name='watchlist',
            field=models.BooleanField(default=False),
        ),
    ]