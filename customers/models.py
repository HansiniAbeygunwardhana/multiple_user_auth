from django.db import models
from users.models import User

# Create your models here.

class Customer(User):
    fullname = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    
    usertype = "customer"
    
    def __str__(self):
        return self.username