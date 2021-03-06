# Generated by Django 3.2.9 on 2021-11-22 16:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('klikaapp', '0002_auto_20211122_1846'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservations',
            name='table_id',
            field=models.ManyToManyField(to='klikaapp.Table'),
        ),
        migrations.AlterField(
            model_name='table',
            name='location_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='klikaapp.location'),
        ),
    ]
