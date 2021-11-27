# Generated by Django 3.2.9 on 2021-11-20 15:57

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0002_auto_20211120_1757'),
    ]

    operations = [
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=200)),
                ('website', models.TextField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('address_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.address')),
                ('user', models.ManyToManyField(to='users.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=200)),
                ('Email', models.EmailField(blank=True, max_length=400, null=True)),
                ('Phone_num', models.CharField(blank=True, max_length=25, null=True)),
                ('num_of_reservations', models.PositiveIntegerField(default=0)),
                ('num_of_cancellations', models.PositiveIntegerField(default=0)),
                ('last_reservation', models.DateTimeField(auto_now_add=True)),
                ('rank', models.IntegerField(blank=True, default=django.db.models.deletion.SET_NULL, null=True)),
                ('comments', models.TextField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('title', models.CharField(max_length=200)),
                ('event_type', models.CharField(blank=True, max_length=200, null=True)),
                ('date', models.DateTimeField(blank=True, null=True)),
                ('entries', models.PositiveIntegerField(blank=True, null=True)),
                ('income', models.FloatField(blank=True, null=True)),
                ('outcome', models.FloatField(blank=True, null=True)),
                ('comments', models.TextField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='table',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('num', models.PositiveSmallIntegerField()),
                ('type', models.CharField(choices=[('bar', 'Bar Table'), ('regular', 'Regular Table'), ('other', 'Other')], max_length=200)),
                ('location', models.CharField(max_length=200)),
                ('sub_location', models.CharField(blank=True, max_length=200, null=True)),
                ('max_persons', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('min_persons', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('business_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='klikaapp.business')),
            ],
        ),
        migrations.CreateModel(
            name='Reservations',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('num_of_persons', models.IntegerField(blank=True, null=True)),
                ('comments', models.TextField(blank=True, null=True)),
                ('cancelled', models.BooleanField(default=False)),
                ('bill', models.FloatField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('business_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='klikaapp.business')),
                ('customer_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='klikaapp.customer')),
                ('event_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='klikaapp.event')),
                ('reserved_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.profile')),
                ('table_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='klikaapp.table')),
            ],
        ),
    ]
