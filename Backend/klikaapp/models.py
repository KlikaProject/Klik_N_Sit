from django.db import models
import uuid
from users.models import Profile, Address


class Customer(models.Model):
    # Primary key
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    # Attributes
    name = models.CharField(max_length=200)
    Email = models.EmailField(max_length=400, null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    Phone_num = models.CharField(max_length=25, null=True, blank=True)
    num_of_reservations = models.PositiveIntegerField(default=0)
    num_of_cancellations = models.PositiveIntegerField(default=0)
    last_reservation = models.DateTimeField(auto_now_add=True)
    rank = models.IntegerField(default=models.SET_NULL, null=True, blank=True)
    comments = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)


class Reservations(models.Model):
    PRIORITIES = (
        (1, 'Low'),
        (2, 'Regular'),
        (3, 'High')
    )

    # Primary key
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    # Attributes
    num_of_persons = models.IntegerField(null=True, blank=True)
    comments = models.TextField(null=True, blank=True)
    cancelled = models.BooleanField(default=False)
    bill = models.FloatField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    priority = models.PositiveSmallIntegerField(choices=PRIORITIES, null=True, blank=True)

    # Foreign keys
    customer = models.ForeignKey('Customer', on_delete=models.SET_NULL, null=True, blank=True)
    business = models.ForeignKey('Business', on_delete=models.SET_NULL, null=True, blank=True)
    event = models.ForeignKey('Event', on_delete=models.SET_NULL, null=True, blank=True)
    reserved_by = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, blank=True)
    table = models.ManyToManyField('Table')

    def __str__(self):
        return 'ID: ' + str(self.id)


class Event(models.Model):
    # Primary key
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    # Attributes
    title = models.CharField(max_length=200)
    event_type = models.CharField(max_length=200, null=True, blank=True)  # maybe change to selection
    date = models.DateField(null=True, blank=True)
    time = models.TimeField(null=True, blank=True)
    entries = models.PositiveIntegerField(null=True, blank=True)
    income = models.FloatField(null=True, blank=True)
    outcome = models.FloatField(null=True, blank=True)
    comments = comments = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Table(models.Model):
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
    #sub_location = models.CharField(max_length=200, null=True, blank=True)
    max_persons = models.PositiveSmallIntegerField(null=True, blank=True)
    min_persons = models.PositiveSmallIntegerField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    priority = models.PositiveSmallIntegerField(null=True, blank=True)

    # Foreign keys
    business = models.ForeignKey('Business', on_delete=models.CASCADE)
    location = models.ForeignKey('Location', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)


class Location(models.Model):

    # Primary key
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    # Attributes
    name = models.CharField(max_length=200)
    priority = models.PositiveSmallIntegerField(null=True, blank=True)

    def __str__(self):
        return str(self.name)


class Business(models.Model):
    # Primary key
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    # Attributes
    name = models.CharField(max_length=200)
    website = models.TextField(null=True, blank=True)
    facebook_link = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    logo = models.ImageField(null=True, blank=True)

    # Foreign keys
    address = models.ForeignKey(Address, on_delete=models.SET_NULL, null=True, blank=True)
    profile = models.ManyToManyField(Profile, null=True, blank=True)

    def __str__(self):
        return self.name

