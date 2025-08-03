from django.contrib import admin
from User_App.models import *


# Register your models here.

class User_Admin(admin.ModelAdmin):
    list_display = ["username","email", "is_superuser", "is_staff", "is_active"]
    list_filter = ["is_superuser", "is_staff", "is_active"]


admin.site.register(User_Model, User_Admin)
