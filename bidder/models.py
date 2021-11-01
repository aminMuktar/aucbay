from django.db import models
from django import forms
# Create your models here.
class bidder (models.Model):
    bidder_id = models.AutoField(primary_key=True)
    bidder_first_name  = models.IntegerField(max_length=30, blank=False)
    bidder_last_name   = models.CharField(max_length=30, blank=False)
    bidder_email       = models.EmailField(max_length=30, blank=False)
   # bidder_password    =   models.CharField(max_length=30, widget=forms.PasswordInput)
    username = models.CharField(max_length=30,blank=False)

