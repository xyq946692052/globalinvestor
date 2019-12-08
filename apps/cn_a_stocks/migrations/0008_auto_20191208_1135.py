# Generated by Django 2.0 on 2019-12-08 03:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cn_a_stocks', '0007_auto_20191203_2024'),
    ]

    operations = [
        migrations.AddField(
            model_name='astocksheader',
            name='business_scope',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='astocksheader',
            name='introduction',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='astocksheader',
            name='main_business',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='astocksheader',
            name='reg_capital',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='astocksheader',
            name='website',
            field=models.URLField(null=True),
        ),
        migrations.AlterField(
            model_name='astocksheader',
            name='ipodate',
            field=models.DateField(blank=True, default=datetime.datetime(2019, 12, 8, 11, 35, 0, 341129), null=True),
        ),
        migrations.AlterField(
            model_name='astocksheader',
            name='outdate',
            field=models.DateField(blank=True, default=datetime.datetime(2019, 12, 8, 11, 35, 0, 341129), null=True),
        ),
    ]