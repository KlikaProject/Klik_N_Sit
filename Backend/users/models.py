from django.db import models
from django.contrib.auth.models import User
import uuid


class Address(models.Model):
    city = models.CharField(max_length=200, null=True, blank=True)
    street = models.CharField(max_length=200, null=True, blank=True)
    Entrance = models.CharField(max_length=200, null=True, blank=True)
    zip_code = models.CharField(max_length=10, null=True, blank=True)
    country = models.CharField(max_length=200, null=True, blank=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)


# TODO: need to modify to null=False, blank=False, after connections users and profiles properly
class Profile(models.Model):
    ROLE_TYPE = (
        ('manager', 'Manager'),
        ('employee', 'Employee')
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(max_length=300, null=True, blank=True)
    birth_date = models.DateTimeField(null=True, blank=True)
    role = models.CharField(max_length=200, choices=ROLE_TYPE)
    address_id = models.ForeignKey('Address', on_delete=models.SET_NULL, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return str(self.user.username)
