from rest_framework import serializers
from klikaapp.models import *
from users.models import *


class Profile_serializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'


class Business_serializer(serializers.ModelSerializer):
    class Meta:
        model = Business
        fields = '__all__'


class Table_serializer(serializers.ModelSerializer):
    business = Business_serializer(many=False)

    class Meta:
        model = Table
        fields = '__all__'
