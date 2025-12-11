from email.policy import default

from django.db import models
from Products_App.models import *
from User_App.models import *
from config import settings


# Create your models here.

class OrderModel(models.Model):
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    is_paid = models.BooleanField(default=False)
    create_at = models.DateTimeField(auto_now_add=True)
    province = models.CharField(null=True, blank=True)
    city = models.CharField(null=True, blank=True)
    address = models.CharField(null=True, blank=True)
    nation_code = models.CharField(null=True, blank=True)

    def __str__(self):
        return f"{self.id} - {self.user} - {self.is_paid}"

class OrderDetails(models.Model):
    order = models.ForeignKey(to=OrderModel, on_delete=models.CASCADE)
    product = models.ForeignKey(to=Product_Model, on_delete=models.CASCADE)
    count = models.IntegerField(default=1)
    off = models.IntegerField(default=0)
    color = models.CharField(null=True, blank=True)

    def __str__(self):
        return f"{self.id} - {self.order.user} - {self.product}"