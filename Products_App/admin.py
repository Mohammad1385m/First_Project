from django.contrib import admin
from Products_App.models import *
# Register your models here.
class ProductsAdmin(admin.ModelAdmin):
    list_display = ["title", "price", "is_active", "category"]
    list_filter = ["is_active", "category"]

admin.site.register(Product_Model, ProductsAdmin)
admin.site.register(Product_Category)
admin.site.register(Product_Color)