from django.db import models
from users.models import User
# Create your models here.

class Staff(User):
    
    branchlist = {
        ('branch1' , 'branch1'),
        ('branch2' , 'branch2'),
        ('branch3' , 'branch3'),
    }
    
    branch = models.CharField(max_length=100  , choices=branchlist , default='branch1')
    tele = models.CharField(max_length=100)
    
    usertype = "staff"
    
    def __str__(self):
        return self.username