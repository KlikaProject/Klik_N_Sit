from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register([Profile, Address])
admin.site.register([Customer, Reservations, Event, Table, Location, Business, ])
