# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from email.policy import default
from pyexpat import model
import random
from statistics import mode
from django.db import models
import base64
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
import datetime

import os
from .models import User
import json
from geopy.geocoders import Nominatim
from django.db.models import Sum, F
from django.db.models.signals import post_save
import qrcode
from io import BytesIO
from django.core.files import File
from PIL import Image, ImageDraw
import uuid
from .managers import GeneralManager
crontab = {}

from django.dispatch import receiver
CURRENCY = '€'

# class Users(models.Model):
#     username=models.CharField(max_length=150)
#     lastname=models.CharField(max_length=150)
#     email=models.CharField(max_length=150) 
#     password1=models.CharField(max_length=150)
#     password2=models.CharField(max_length=150)
#     referral_code=models.CharField(max_length=150)
#     phone=models.CharField(max_length=150)
#     postcode=models.CharField(max_length=150)
# from django.contrib.auth.models import AbstractUser
from django.db import models




class Employee(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(
        User, 
        on_delete=models.CASCADE,
        null=True,
        blank=True,related_name='account'
    )
    referral_code=models.TextField(max_length=150)
    phone=models.BigIntegerField()

    postcode=models.TextField(max_length=150)
    referral=models.CharField(max_length=150)
    designation=models.ForeignKey(
        'roles', 
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    business=models.ForeignKey(
        'business_details', 
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    
    
class PaymentMethod(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(unique=True, max_length=150)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = '0. Payment Method'



class Transactions(models.Model): 
        id = models.AutoField(primary_key=True)     
        price = models.CharField(max_length=200)
        session_id = models.CharField(max_length=200)
        Customer=models.CharField(max_length=200)
        status = models.CharField(max_length=20,default='pending')
class Meta:
        verbose_name_plural = 'price'
def __str__(self):
        return self.price

    


class mobile(models.Model):
    id = models.AutoField(primary_key=True)
    sId=models.IntegerField()
    phone=models.CharField(max_length=50)


class business_details(models.Model):
    id = models.AutoField(primary_key=True)
    categories=models.ForeignKey(
        'category',
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    bank_name=models.CharField(max_length=50)
    latitude = models.TextField(max_length=150)
    longitude = models.TextField(max_length=150)
    business_name=models.CharField(max_length=50)
    business_desc=models.CharField(max_length=200)
    business_address=models.CharField(max_length=200)
    email=models.EmailField(max_length=50)
    subcategory=models.CharField(max_length=200)
    irich=models.FloatField(default=1)    
    business_code=models.CharField(max_length=50)
    Account_details=models.CharField(max_length=50)
    account_number=models.CharField(max_length=50)
    IFSC_code=models.CharField(max_length=50)
    business_contact=models.CharField(max_length=50)
    image1= models.ImageField(upload_to='images',blank= True,null=True)
    user=models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    qr_code=models.ImageField(upload_to='qr_codes', blank=True)

    def save(self, *args, **kwargs):
        qrcode_image = qrcode.make(self.get_qr_url())
        canvas = Image.new("RGB", (400, 400), "white")
        draw = ImageDraw.Draw(canvas)
        canvas.paste(qrcode_image)
        buffer = BytesIO()
        canvas.save(buffer, "PNG")
       
        canvas.close()
        super().save(*args, **kwargs)

    def get_qr_url(self):
        return 'http://13.232.49.240:8000/payment.html'

    
        # return stream.getvalue().decode()
        
    # qrcode = property(_get_qrcode)


    def __str__(self):
        return self.business_name

class category(models.Model):
    id = models.AutoField(primary_key=True)
    name=models.TextField(max_length=500)

    def __str__(self):
        return self.name

class roles(models.Model):
    id = models.AutoField(primary_key=True)
    designation=models.CharField(max_length=500)


class deals(models.Model):
    id = models.AutoField(primary_key=True)
    title=models.CharField(max_length=500)
    description=models.CharField(max_length=500)

class rewards(models.Model):
    id = models.AutoField(primary_key=True)
    start_date=models.DateField()
    end_date=models.DateField()
    targeted_amount=models.CharField(max_length=500)
    referral_member=models.CharField(max_length=500, null=True)
    description = models.CharField(max_length=500)

class payments(models.Model):
    id = models.AutoField(primary_key=True)
    amount=models.IntegerField()
    irich_bonus = models.FloatField(default=0)
    business=models.ForeignKey(
        business_details,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        # verbose_name='business_name'
    )
    user=models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        # verbose_name='business_name'
    )
    irich_walletamount = models.ForeignKey(
        'wallet',
        on_delete=models.CASCADE,
        null=True,
        blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
class wallet(models.Model):
    id = models.AutoField(primary_key=True)
    earning=models.CharField(max_length=50)
    irich_bonus=models.CharField(max_length=100)
    starting_irich_bonus=models.IntegerField(max_length=100, default=0)
    user=models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        # verbose_name='business_name'
    )

    def __str__(self):
        return str(self.user)

class PaymentProcessComplete(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    payment_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = 'payment_process_complete'

