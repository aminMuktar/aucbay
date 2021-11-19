# Generated by Django 3.2.8 on 2021-11-19 11:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField(unique=True)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=255, verbose_name='Item Name')),
                ('item_price', models.DecimalField(decimal_places=2, max_digits=12, verbose_name='Item price')),
                ('item_img', models.ImageField(blank=True, null=True, upload_to='uploads/', verbose_name='Item img')),
                ('item_description', models.CharField(max_length=400, verbose_name='Item Description')),
                ('item_location', models.CharField(max_length=20, verbose_name='Item Location')),
                ('item_remaining_time', models.DateTimeField(verbose_name='Item Remaining Time')),
                ('ispection_start', models.DateTimeField(verbose_name='Ispection Start')),
                ('ispection_end', models.DateTimeField(verbose_name='Ispection End')),
                ('min_increment', models.IntegerField(verbose_name='Min Increment')),
                ('attribute', models.CharField(max_length=255, verbose_name='Attribute')),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to='uploads/', verbose_name='Thumbnail')),
                ('item_date_added', models.DateTimeField(auto_now_add=True, verbose_name='Item Date Added')),
                ('slug', models.SlugField(unique=True)),
                ('Category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='item', to='item.category')),
            ],
            options={
                'ordering': ('item_date_added',),
            },
        ),
    ]
