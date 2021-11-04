from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

class bidder(AbstractBaseUser, PermissionsMixin):

     bidder_id = models.AutoField(primary_key=True)
     bidder_firstname   = models.CharField(max_length=30, blank=False)
     bidder_lastname    = models.CharField(max_length=30, blank=False)
     bidder_email       = models.EmailField(max_length=30, blank=False,null=True,unique=True,)
     bidder_password    =   models.CharField(max_length=30,default="", editable=False)
     username           = models.CharField(max_length=30,blank=False)

     
     USERNAME_FIELD = 'bidder_email'
     REQUIRED_FIELDS = ['username', 'bidder_firstname']

     def __str__(self):
        return self.username
    

