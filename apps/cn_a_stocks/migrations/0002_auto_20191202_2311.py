# Generated by Django 2.0 on 2019-12-02 15:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cn_a_stocks', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='astockscategory',
            old_name='name',
            new_name='category_name',
        ),
    ]
