from django.db import models
from django.db.models.base import Model
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
class auctioneer (AbstractBaseUser,PermissionsMixin):
    auctioneer_id           = models.AutoField(primary_key=True)
    auctioneer_firstname    = models.CharField(max_length=30)
    auctioneer_lastname     = models.CharField(max_length=30)
    auctioneer_email        = models.EmailField(max_length=30)
    auctioneer_pasword      = models.CharField(max_length=30)
    username                =models.CharField(max_length=30)
    USERNAME_FIELD = "username"
    REQUIRED_FIELD = "auctioneer_firstname"
    def __str__ (self):
        return self.username
   