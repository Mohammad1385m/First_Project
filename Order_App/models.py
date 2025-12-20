from django.utils import timezone
from email.policy import default

from django.db import models
from django.utils.crypto import get_random_string

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
    factor_id = models.CharField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.factor_id:
            year = timezone.now().year
            random_part = get_random_string(length=3,
                                            allowed_chars="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz")
            id_padded = str(self.id).zfill(3)
            print(self.id, id_padded)
            self.factor_id = f"DGT-{random_part}-{id_padded}-{year}"
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.id} - {self.user} - {self.is_paid}"

    def total_cost(self):
        if self.is_paid:
            total = 0
            for item in self.orderdetails_set.all():
                total += item.final_price * item.count
            return total
        else:
            pass


class OrderDetails(models.Model):
    order = models.ForeignKey(to=OrderModel, on_delete=models.CASCADE)
    product = models.ForeignKey(to=Product_Model, on_delete=models.CASCADE)
    count = models.IntegerField(default=1)
    off = models.IntegerField(default=0)
    color = models.CharField(null=True, blank=True)
    final_price = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.order.id} - {self.order.user} - {self.product}"

    def discount(self):
        return self.final_price - (self.final_price * (self.off / 100))

    def total_price(self):
        return self.discount() * self.count
