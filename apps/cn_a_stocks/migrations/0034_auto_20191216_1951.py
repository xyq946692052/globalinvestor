# Generated by Django 2.0 on 2019-12-16 11:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cn_a_stocks', '0033_auto_20191216_1611'),
    ]

    operations = [
        migrations.AlterField(
            model_name='astocksheader',
            name='ipodate',
            field=models.DateField(blank=True, default=datetime.datetime(2019, 12, 16, 19, 51, 19, 523575), null=True),
        ),
        migrations.AlterField(
            model_name='astocksheader',
            name='outdate',
            field=models.DateField(blank=True, default=datetime.datetime(2019, 12, 16, 19, 51, 19, 523575), null=True),
        ),
    ]
