from datetime import timezone
import datetime
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import CustomUserManager

class User(AbstractBaseUser, PermissionsMixin):
    
    USER_TYPE = (
        ('Admin', 'Admin'),
        ('Customer', 'Customer'),
        ('Staff', 'Staff')
    )
    
    user_type = models.CharField(max_length=20, choices=USER_TYPE)
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=200, verbose_name='first name')
    last_name = models.CharField(max_length=200, verbose_name='first name')
    dob = models.DateTimeField(verbose_name='Date of Birth',  blank=True,  default=datetime.datetime(2000, 1, 1, 0, 0))
    phone_number = models.CharField(max_length=15)
    loaction = models.CharField(max_length=20)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    
    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []    
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
