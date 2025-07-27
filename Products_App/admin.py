from django.contrib import admin
from Products_App.models import *
# Register your models here.
class ProductsAdmin(admin.ModelAdmin):
    list_display = ["title", "price", "is_active", "subcategory", "category"]
    list_filter = ["is_active", "subcategory", "subcategory__category"]

class subcategoryAdmin(admin.ModelAdmin):
    list_display = ["title", "is_active", "category"]
    list_filter = ["is_active", "category"]

class categoryAdmin(admin.ModelAdmin):
    list_display = ["title", "is_active"]
    list_filter = ["is_active"]

class colorAdmin(admin.ModelAdmin):
    list_display=["color_name", "hex_code"]

admin.site.register(Product_Model, ProductsAdmin)
admin.site.register(Product_SubCategory, subcategoryAdmin)
admin.site.register(Product_Category, categoryAdmin)
admin.site.register(Product_Color, colorAdmin)