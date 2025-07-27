from django.contrib import admin
from Contact_Us_App.models import *

# Register your models here.

class ContactUsAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "subject", "is_read"]
    list_filter = ["subject", "is_read"]

admin.site.register(Contact_Us_Model, ContactUsAdmin)
