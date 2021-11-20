from django.db import models
import uuid
from users.models import Profile


class Customer(models.Model):
    # Primary key
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    # Attributes
    name = models.CharField(max_length=200)
    Email = models.EmailField(max_length=400, null=True, blank=True)
    Phone_num = models.CharField(max_length=25, null=True, blank=True)
    num_of_reservations = models.IntegerField(default=0)
    num_of_cancellations = models.IntegerField(default=0)
    last_reservation = models.DateTimeField(auto_now_add=True)
    rank = models.IntegerField(default= models.SET_NULL, null=True, blank=True)
    comments = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)


class Reservations(models.Model):
    # Primary key
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    # Attributes
    num_of_persons = models.IntegerField(null=True, blank=True)
    comments = models.TextField(null=True, blank=True)
    cancelled = models.BooleanField(default=False)
    bill = models.FloatField(null=True, blank=True)

    # Foreign keys
    customer_id = models.ForeignKey('Customer')
    table_id = models.ForeignKey('Table')
    business_id = models.ForeignKey('Business')
    event_id = models.ForeignKey('Event')
    reserved_by = models.ForeignKey(Profile)
    created = models.DateTimeField(auto_now_add=True)


class Event(models.Model):
    # Primary key
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    # Attributes
    title = models.CharField(max_length=200)
    event_type = models.CharField(max_length=200, null=True, blank=True)  # maybe change to selection
    date = models.DateTimeField(null=True, blank=True)
    entries = models.IntegerField(null=True, blank=True)
    income = models.FloatField(null=True, blank=True)
    outcome = models.FloatField(null=True, blank=True)
    comments = comments = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)


class table(models.Model):
    TABLE_TYPE = (
        ('bar', 'Bar Table'),
        ('regular', 'Regular Table'),
        ('other', 'Other')
    )

    # Primary key
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    # Attributes
    num = models.IntegerField(null=True, blank=True)
    type = models.CharField(choices=TABLE_TYPE)
    location = models.CharField(max_length=200)
    sub_location = models.CharField(max_length=200, null=True, blank=True)
    max_persons = models.IntegerField(null=True, blank=True)
    min_persons = models.IntegerField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    # Foreign keys
    business_id = models.ForeignKey('Business')

