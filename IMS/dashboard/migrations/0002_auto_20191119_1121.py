# Generated by Django 2.2.7 on 2019-11-19 11:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='inventory',
            old_name='inv_category',
            new_name='inventory_category',
        ),
        migrations.RenameField(
            model_name='inventory',
            old_name='inv_description',
            new_name='inventory_description',
        ),
        migrations.RenameField(
            model_name='inventory',
            old_name='measure_unit',
            new_name='measure_Unit',
        ),
    ]
