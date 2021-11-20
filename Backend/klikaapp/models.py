from django.db import models
import uuid
from users.models import Profile, Address


class Customer(models.Model):
    # Primary key
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    # Attributes
    name = models.CharField(max_length=200)
    Email = models.EmailField(max_length=400, null=True, blank=True)
    Phone_num = models.CharField(max_length=25, null=True, blank=True)
    num_of_reservations = models.PositiveIntegerField(default=0)
    num_of_cancellations = models.PositiveIntegerField(default=0)
    last_reservation = models.DateTimeField(auto_now_add=True)
    rank = models.IntegerField(default= models.SET_NULL, null=True, blank=True)
    comments = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)


class Reservations(models.Model):
    # Primary key
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    # Attributes
    num_of_persons = models.IntegerField(null=True, blank=True)
    comments = models.TextField(null=True, blank=True)
    cancelled = models.BooleanField(default=False)
    bill = models.FloatField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    # Foreign keys
    customer_id = models.ForeignKey('Customer', on_delete=models.SET_NULL, null=True, blank=True)
    table_id = models.ForeignKey('Table', on_delete=models.SET_NULL, null=True, blank=True)
    business_id = models.ForeignKey('Business', on_delete=models.SET_NULL, null=True, blank=True)
    event_id = models.ForeignKey('Event', on_delete=models.SET_NULL, null=True, blank=True)
    reserved_by = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return 'ID: ' + str(self.id) + ', Customer: ' + str(self.customer_id.name)


class Event(models.Model):
    # Primary key
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    # Attributes
    title = models.CharField(max_length=200)
    event_type = models.CharField(max_length=200, null=True, blank=True)  # maybe change to selection
    date = models.DateTimeField(null=True, blank=True)
    entries = models.PositiveIntegerField(null=True, blank=True)
    income = models.FloatField(null=True, blank=True)
    outcome = models.FloatField(null=True, blank=True)
    comments = comments = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class table(models.Model):
    TABLE_TYPE = (
        ('bar', 'Bar Table'),
        ('regular', 'Regular Table'),
        ('other', 'Other')
    )

    # Primary key
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    # Attributes
    num = models.PositiveSmallIntegerField()
    type = models.CharField(max_length=200, choices=TABLE_TYPE)
    location = models.CharField(max_length=200)
    sub_location = models.CharField(max_length=200, null=True, blank=True)
    max_persons = models.PositiveSmallIntegerField(null=True, blank=True)
    min_persons = models.PositiveSmallIntegerField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    # Foreign keys
    business_id = models.ForeignKey('Business', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.num) + ', ' + str(self.business_id.name)


class Business(models.Model):
    # Primary key
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    # Attributes
    name = models.CharField(max_length=200)
    website = models.TextField( null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    # Foreign keys
    address_id = models.ForeignKey(Address, on_delete=models.SET_NULL, null=True, blank=True)
    user = models.ManyToManyField(Profile)

    def __str__(self):
        return self.name

