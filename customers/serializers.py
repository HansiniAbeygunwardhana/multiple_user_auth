from rest_framework import serializers
from .models import Customer
from users.serializers import UserSerializer

class CustomerSerializer(UserSerializer):
    class Meta:
        model = Customer
        fields = ['fullname' , 'address' , 'username' , 'password' , 'email']