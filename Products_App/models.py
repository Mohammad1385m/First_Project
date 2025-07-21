from enum import unique

from django.db import models


# Create your models here.

class Product_Category(models.Model):
    title = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    slug = models.SlugField(unique=True, null=True, blank=True)

    def save(self, *args, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug = self.title.replace(" ", "_")
        super().save(force_insert, force_update, using, update_fields)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class Product_Model(models.Model):
    title = models.CharField()
    price = models.IntegerField()
    off = models.IntegerField(default=0)
    description = models.TextField(null=True)
    color = models.ManyToManyField(to="Product_Color")
    category = models.ForeignKey(Product_Category, on_delete=models.CASCADE, null=True)
    is_active = models.BooleanField(default=True)
    slug = models.SlugField(unique=True, null=True, blank=True)

    def save(self, *args, force_insert=False, force_update=False, using=None, update_fields=None, ):
        self.slug = self.title.replace(" ", "_")
        super().save(*args, force_insert=False, force_update=False, using=None, update_fields=None, )

    def __str__(self):
        return f"{self.title} - {self.price}"

    class Meta:
        verbose_name = "Product Model"
        verbose_name_plural = "Product Models"

class Product_Color(models.Model):
    color_name = models.CharField()
    hex_code = models.CharField()

    def __str__(self):
        return f"{self.color_name} - {self.hex_code}"

    class Meta:
        verbose_name = "Color"
        verbose_name_plural = "Colors"