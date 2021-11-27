from rest_framework import serializers
from klikaapp.models import *
from users.models import *
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self):
        user = User(
            email=self.validated_data['email'],
            username=self.validated_data['username'],
            first_name=self.validated_data['first_name'],
            last_name=self.validated_data['last_name']
        )
        user.set_password(self.validated_data['password']),
        user.save()

        return user


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'

    def save(self):
        profile = Profile(
            name=self.validated_data['name'],
            birth_date=self.validated_data['birth_date'],
            role=self.validated_data['role'],
            address=self.validated_data['address_id'],
            #user=self.validated_data['user_id'],
        )
        profile.save()

        return profile


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'


class BusinessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Business
        fields = '__all__'


class TableSerializer(serializers.ModelSerializer):
    business = BusinessSerializer(many=False)

    class Meta:
        model = Table
        fields = '__all__'
