from rest_framework import serializers
from .models import Staff
from users.serializers import UserSerializer

class StaffSerializer(UserSerializer):
    class Meta:
        model = Staff
        fields = ['branch' , 'tele'  , 'username' , 'password' , 'email' , 'usertype']