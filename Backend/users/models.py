from django.db import models
from django.contrib.auth.models import User
import uuid


class Address(models.Model):
    # Primary key
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    # Attributes
    city = models.CharField(max_length=200, null=True, blank=True)
    street = models.CharField(max_length=200, null=True, blank=True)
    Entrance = models.CharField(max_length=200, null=True, blank=True)
    zip_code = models.CharField(max_length=10, null=True, blank=True)
    country = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return str(self.street) + ', ' + str(self.city) + ', ' + str(self.Entrance) + ', ' + str(self.country)


# TODO: need to modify to null=False, blank=False, after connections users and profiles properly
class Profile(models.Model):
    ROLE_TYPE = (
        ('manager', 'Manager'),
        ('employee', 'Employee')
    )

    # Primary key
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    # Attributes
    name = models.CharField(max_length=200, null=True, blank=True)
    #email = models.EmailField(max_length=300, null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    role = models.CharField(max_length=200, choices=ROLE_TYPE)
    created = models.DateTimeField(auto_now_add=True)
    num_of_logins = models.PositiveIntegerField(default=0)
    last_login = models.DateTimeField(null=True, blank=True)

    # Foreign keys
    address = models.ForeignKey('Address', on_delete=models.SET_NULL, null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return str(self.name)
