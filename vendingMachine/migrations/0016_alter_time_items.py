# Generated by Django 4.1.6 on 2023-02-07 23:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendingMachine', '0015_remove_time_items_time_items'),
    ]

    operations = [
        migrations.AlterField(
            model_name='time',
            name='items',
            field=models.TextField(null=True),
        ),
    ]
