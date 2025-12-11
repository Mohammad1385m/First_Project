from django.contrib import admin
from Products_App.models import *


# Register your models here.
class ProductsAdmin(admin.ModelAdmin):
    list_display = ["title", "price", "is_active", "category", "brand"]
    list_filter = ["is_active", "category", "brand"]
    list_editable = ["is_active", "price"]


class BrandAdmin(admin.ModelAdmin):
    list_display = ["title", "is_active"]
    list_filter = ["is_active"]


class CategoryAdmin(admin.ModelAdmin):
    list_display = ["title", "is_active"]
    list_filter = ["is_active"]


class ColorAdmin(admin.ModelAdmin):
    list_display = ["color_name", "hex_code"]


class ExtraImagesAdmin(admin.ModelAdmin):
    list_display = ["product_title", "product_id", "image"]
    list_filter = ["product__title"]

    def product_title(self, obj):
        return obj.product.title


admin.site.register(Product_Model, ProductsAdmin)
admin.site.register(BrandModel, BrandAdmin)
admin.site.register(Product_Category, CategoryAdmin)
admin.site.register(Product_Color, ColorAdmin)
admin.site.register(Product_Extra_Images, ExtraImagesAdmin)
