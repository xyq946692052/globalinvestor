# Generated by Django 2.0 on 2019-12-16 07:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cn_a_stocks', '0030_auto_20191216_1549'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='EarnRate',
            new_name='AStocksEarnRate',
        ),
        migrations.AlterField(
            model_name='astocksheader',
            name='ipodate',
            field=models.DateField(blank=True, default=datetime.datetime(2019, 12, 16, 15, 53, 45, 473897), null=True),
        ),
        migrations.AlterField(
            model_name='astocksheader',
            name='outdate',
            field=models.DateField(blank=True, default=datetime.datetime(2019, 12, 16, 15, 53, 45, 473897), null=True),
        ),
    ]
