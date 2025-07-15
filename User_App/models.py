from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class User_Model(AbstractUser):
    phone_number = models.CharField(max_length=11, unique=True)
    # avtar = models.ImageField(upload_to="user_avatars/%y%m%d", null=True, blank=True)