# Generated by Django 2.0 on 2019-12-12 03:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cn_a_stocks', '0020_auto_20191212_1115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='astocksheader',
            name='ipodate',
            field=models.DateField(blank=True, default=datetime.datetime(2019, 12, 12, 11, 20, 2, 546826), null=True),
        ),
        migrations.AlterField(
            model_name='astocksheader',
            name='outdate',
            field=models.DateField(blank=True, default=datetime.datetime(2019, 12, 12, 11, 20, 2, 546826), null=True),
        ),
        migrations.AlterModelTable(
            name='astocksprofit',
            table='stocks_a_profile',
        ),
    ]
