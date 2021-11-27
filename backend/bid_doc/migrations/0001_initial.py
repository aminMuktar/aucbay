# Generated by Django 3.2.8 on 2021-11-11 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='biddoc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('denial_of_val', models.IntegerField(verbose_name='Denial of Validity')),
                ('init_price', models.FloatField(verbose_name='Initial Price')),
                ('deadline', models.DateTimeField(verbose_name='Deadline')),
                ('bidCount', models.IntegerField(verbose_name='Bid Count')),
                ('highBidder', models.BooleanField(default=False, verbose_name='High Bidder')),
                ('auctionStatus', models.BooleanField(default=True, verbose_name='Auction Status')),
                ('bid_doc_created_at', models.DateTimeField(auto_now_add=True)),
                ('slug', models.SlugField(unique=True)),
            ],
            options={
                'ordering': ('deadline',),
            },
        ),
    ]
