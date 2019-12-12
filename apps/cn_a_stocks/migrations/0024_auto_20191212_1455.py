# Generated by Django 2.0 on 2019-12-12 06:55

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cn_a_stocks', '0023_auto_20191212_1258'),
    ]

    operations = [
        migrations.CreateModel(
            name='AStocksGrowth',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pub_date', models.DateField(null=True)),
                ('stat_date', models.DateField(null=True)),
                ('yoyequity', models.FloatField()),
                ('yoy_asset', models.FloatField()),
                ('yoy_ni', models.FloatField()),
                ('yoy_eps_basic', models.FloatField()),
                ('yoy_pni', models.FloatField()),
            ],
            options={
                'db_table': 'stocks_a_growth',
            },
        ),
        migrations.AlterField(
            model_name='astocksheader',
            name='ipodate',
            field=models.DateField(blank=True, default=datetime.datetime(2019, 12, 12, 14, 55, 54, 826927), null=True),
        ),
        migrations.AlterField(
            model_name='astocksheader',
            name='outdate',
            field=models.DateField(blank=True, default=datetime.datetime(2019, 12, 12, 14, 55, 54, 826927), null=True),
        ),
        migrations.AddField(
            model_name='astocksgrowth',
            name='stock',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cn_a_stocks.AStocksHeader'),
        ),
    ]