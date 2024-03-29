# Generated by Django 2.2.7 on 2019-11-19 11:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Measure',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('measure', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inv_category', models.CharField(max_length=250)),
                ('inv_description', models.CharField(max_length=250)),
                ('measure_unit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.Measure')),
            ],
        ),
    ]
