# Generated by Django 4.0.3 on 2022-04-05 17:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='resque',
            old_name='address',
            new_name='addrs',
        ),
    ]