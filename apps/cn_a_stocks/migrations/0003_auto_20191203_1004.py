# Generated by Django 2.0 on 2019-12-03 02:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cn_a_stocks', '0002_auto_20191202_2311'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='astocksheader',
            options={'ordering': ('stock_code',)},
        ),
    ]