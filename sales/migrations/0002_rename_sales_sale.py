# Generated by Django 3.2.7 on 2021-10-05 07:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_auto_20211005_1156'),
        ('sales', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Sales',
            new_name='Sale',
        ),
    ]
