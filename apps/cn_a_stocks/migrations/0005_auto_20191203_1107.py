# Generated by Django 2.0 on 2019-12-03 03:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cn_a_stocks', '0004_astocksheader_area'),
    ]

    operations = [
        migrations.AddField(
            model_name='astocksheader',
            name='ipodate',
            field=models.DateField(default=datetime.datetime(2019, 12, 3, 11, 7, 12, 327609)),
        ),
        migrations.AddField(
            model_name='astocksheader',
            name='outdate',
            field=models.DateField(default=datetime.datetime(2019, 12, 3, 11, 7, 12, 327609)),
        ),
    ]
