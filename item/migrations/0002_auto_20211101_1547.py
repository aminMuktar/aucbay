# Generated by Django 3.2.8 on 2021-11-01 12:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='Category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='item', to='item.category'),
        ),
        migrations.AlterField(
            model_name='items',
            name='item_img',
            field=models.ImageField(null=True, upload_to='uploads/'),
        ),
    ]
