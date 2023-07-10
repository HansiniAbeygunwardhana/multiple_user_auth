from django.contrib.auth.models import AbstractUser
from django.db import models
from rest_framework.serializers import ModelSerializer
from django.contrib.auth.hashers import make_password

class User(AbstractUser):
    
    usertypelist = {
        ('customer' , 'customer'),
        ('staff' , 'staff'),
        ('manager' , 'manager'),
    }
    usertype = models.CharField(max_length=10 , choices=usertypelist , default='customer')
    
    
    def set_password(self, raw_password):
        self.password = make_password(raw_password)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.set_password(self.password)
        super().save(*args, **kwargs)