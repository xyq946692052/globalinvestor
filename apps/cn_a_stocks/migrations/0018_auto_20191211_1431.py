# Generated by Django 2.0 on 2019-12-11 06:31

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cn_a_stocks', '0017_auto_20191210_1207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='astocksheader',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='cn_a_stocks.AStocksCategory'),
        ),
        migrations.AlterField(
            model_name='astocksheader',
            name='ipodate',
            field=models.DateField(blank=True, default=datetime.datetime(2019, 12, 11, 14, 31, 36, 520050), null=True),
        ),
        migrations.AlterField(
            model_name='astocksheader',
            name='outdate',
            field=models.DateField(blank=True, default=datetime.datetime(2019, 12, 11, 14, 31, 36, 520050), null=True),
        ),
    ]
