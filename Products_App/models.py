from sys import maxsize
from django.db import models

# Create your models here.

"""
*****************************************################*****************************************
*****************************************##  Category  ##*****************************************
*****************************************################*****************************************
"""
class Product_Category(models.Model):
    title = models.CharField()
    is_active = models.BooleanField(default=True)
    slug = models.SlugField(unique=True, null=True, blank=True)

    def save(self, *args, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug = self.title.replace(" ", "_")
        super().save(*args, force_insert=False, force_update=False, using=None, update_fields=None)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

"""
********************************************#############********************************************
********************************************##  Brand  ##********************************************
********************************************#############********************************************
"""
class BrandModel(models.Model):
    title = models.CharField()
    is_active = models.BooleanField(default=True)
    slug = models.SlugField(unique=True, null=True, blank=True)

    def save(self, *args, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug = self.title.replace(" ", "_")
        super().save(*args, force_insert=False, force_update=False, using=None, update_fields=None)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "Brand"
        verbose_name_plural = "Brands"
"""
*****************************************###############*****************************************
*****************************************##  Product  ##*****************************************
*****************************************###############*****************************************
"""
class Product_Model(models.Model):
    title = models.CharField()
    price = models.IntegerField()
    off = models.IntegerField(default=0)
    description = models.TextField()
    color = models.ManyToManyField(to="Product_Color")
    main_image = models.ImageField(upload_to="products/", null=True, blank=True)
    # subcategory = models.ForeignKey(to=Product_SubCategory, on_delete=models.CASCADE)
    category = models.ForeignKey(to=Product_Category, on_delete=models.CASCADE)
    brand = models.ForeignKey(to=BrandModel, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    slug = models.SlugField(unique=True, null=True, blank=True)

    def save(self, *args, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug = self.title.replace(" ", "_")
        super().save(*args, force_insert=False, force_update=False, using=None, update_fields=None)

    def __str__(self):
        return f"{self.title} - {self.price}"

    class Meta:
        verbose_name = "Product Model"
        verbose_name_plural = "Product Models"

"""
*****************************************#############*****************************************
*****************************************##  Color  ##*****************************************
*****************************************#############*****************************************
"""
class Product_Color(models.Model):
    color_name = models.CharField()
    hex_code = models.CharField()

    def __str__(self):
        return f"{self.color_name} - {self.hex_code}"

    class Meta:
        verbose_name = "Color"
        verbose_name_plural = "Colors"

"""
*****************************************#############*****************************************
*****************************************##  Image  ##*****************************************
*****************************************#############*****************************************
"""
class Product_Extra_Images(models.Model):
    product = models.ForeignKey(to=Product_Model, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="products/extra/")