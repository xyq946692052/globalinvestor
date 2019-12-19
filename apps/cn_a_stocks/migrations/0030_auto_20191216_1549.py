# Generated by Django 2.0 on 2019-12-16 07:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cn_a_stocks', '0029_auto_20191216_1001'),
    ]

    operations = [
        migrations.CreateModel(
            name='EarnRate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('one_month', models.TextField()),
                ('three_month', models.TextField()),
                ('half_year', models.TextField()),
                ('one_year', models.TextField()),
                ('three_year', models.TextField()),
            ],
            options={
                'db_table': 'stocks_a_earnrate',
            },
        ),
        migrations.AlterField(
            model_name='astocksheader',
            name='ipodate',
            field=models.DateField(blank=True, default=datetime.datetime(2019, 12, 16, 15, 49, 53, 631391), null=True),
        ),
        migrations.AlterField(
            model_name='astocksheader',
            name='outdate',
            field=models.DateField(blank=True, default=datetime.datetime(2019, 12, 16, 15, 49, 53, 631391), null=True),
        ),
    ]