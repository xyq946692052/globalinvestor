# Generated by Django 2.0 on 2019-12-03 12:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cn_a_stocks', '0006_auto_20191203_1436'),
    ]

    operations = [
        migrations.AlterField(
            model_name='astocksheader',
            name='ipodate',
            field=models.DateField(default=datetime.datetime(2019, 12, 3, 20, 24, 18, 399852)),
        ),
        migrations.AlterField(
            model_name='astocksheader',
            name='outdate',
            field=models.DateField(default=datetime.datetime(2019, 12, 3, 20, 24, 18, 399852)),
        ),
    ]
