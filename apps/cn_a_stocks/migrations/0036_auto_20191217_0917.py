# Generated by Django 2.0 on 2019-12-17 01:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cn_a_stocks', '0035_auto_20191216_2233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='astocksheader',
            name='ipodate',
            field=models.DateField(blank=True, default=datetime.datetime(2019, 12, 17, 9, 17, 42, 540021), null=True),
        ),
        migrations.AlterField(
            model_name='astocksheader',
            name='outdate',
            field=models.DateField(blank=True, default=datetime.datetime(2019, 12, 17, 9, 17, 42, 540021), null=True),
        ),
    ]
