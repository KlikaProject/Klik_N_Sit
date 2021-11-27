# Generated by Django 3.2.9 on 2021-11-23 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('klikaapp', '0006_auto_20211122_1904'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='birth_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='reservations',
            name='table',
            field=models.ManyToManyField(to='klikaapp.Table'),
        ),
    ]