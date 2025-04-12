from django.db import models
from django.contrib.auth.models import AbstractUser
from users.managers import CustomUserManager 

class User(AbstractUser):
    username = None
    email = models.EmailField(max_length=100,unique=True)
    address = models.CharField(max_length=100,null=True,blank=True)
    phone_number = models.CharField(max_length=15, blank=True, null = True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()
    def __str__(self):
        return self.email
