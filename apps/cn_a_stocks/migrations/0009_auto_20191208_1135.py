# Generated by Django 2.0 on 2019-12-08 03:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cn_a_stocks', '0008_auto_20191208_1135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='astocksheader',
            name='ipodate',
            field=models.DateField(blank=True, default=datetime.datetime(2019, 12, 8, 11, 35, 22, 560400), null=True),
        ),
        migrations.AlterField(
            model_name='astocksheader',
            name='outdate',
            field=models.DateField(blank=True, default=datetime.datetime(2019, 12, 8, 11, 35, 22, 560400), null=True),
        ),
    ]
