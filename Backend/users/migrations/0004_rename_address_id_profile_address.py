# Generated by Django 3.2.9 on 2021-11-27 08:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_profile_birth_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='address_id',
            new_name='address',
        ),
    ]
