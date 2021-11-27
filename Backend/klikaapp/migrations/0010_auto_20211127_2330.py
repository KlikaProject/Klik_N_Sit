# Generated by Django 3.2.9 on 2021-11-27 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_remove_profile_email'),
        ('klikaapp', '0009_alter_reservations_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='business',
            name='profile',
            field=models.ManyToManyField(blank=True, to='users.Profile'),
        ),
        migrations.AlterField(
            model_name='reservations',
            name='table',
            field=models.ManyToManyField(to='klikaapp.Table'),
        ),
    ]