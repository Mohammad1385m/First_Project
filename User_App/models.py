from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

"""
Super User:
mhmd (m12345)
"""


class User_Model(AbstractUser):
    email = models.EmailField(unique=True, null=False, blank=False)
    phone = models.CharField(null=True)
    avtar = models.ImageField(upload_to="user_avatars/%y%m%d", null=True, blank=True)
    token = models.CharField(null=True, blank=True)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"


# class Otp_Model(models.Model):
#     user = models.ForeignKey(to=User_Model, on_delete=models.CASCADE)
#     code = models.CharField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     errors = models.IntegerField(default=0)
#
#     def __str__(self):
#         return self.code
#
#     def otp_timer_validation(self):
#         if self.created_at + timedelta(minutes=3) > timezone.now():
#             return True
#         else:
#             return False
#
#     class Meta:
#         verbose_name = "OTP"
#         verbose_name_plural = "OTPs"
