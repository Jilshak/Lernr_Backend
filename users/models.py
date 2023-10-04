from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import UserManager

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True, max_length=100)
    username = models.CharField(max_length=200, blank=True, null=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    profile_image = models.ImageField(blank=True, null=True, upload_to='profile')
    is_instructor = models.BooleanField(default=False)
    is_user = models.BooleanField(default=True)
    is_blocked = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
    is_authorized = models.BooleanField(default=True)
    
    
    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserManager()
    

    def __str__(self):
        return self.email