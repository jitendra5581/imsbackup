# Generated by Django 2.2.7 on 2019-11-19 12:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_auto_20191119_1121'),
    ]

    operations = [
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('purchase_date', models.DateField()),
                ('frontend_quantity', models.IntegerField()),
                ('purchase_price', models.FloatField()),
                ('backend_measure', models.CharField(max_length=100)),
                ('backend_quantity', models.IntegerField()),
                ('frontend_measure', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.Measure')),
                ('inventory_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.Inventory')),
            ],
        ),
    ]