from django.contrib import admin
from .models import *

# Register your models here.

class Blog_Content_InLine(admin.TabularInline):
    model = Block_Content_Model
    extra = 0
    fields = ["block_type", "text", "image", "caption", "order"]
    ordering = ["order"]

class Blog_Admin(admin.ModelAdmin):
    inlines = [Blog_Content_InLine]
    prepopulated_fields = {
        "slug": ["title"]
    }
    def save_model(self, request, obj, form, change):
        if change:
            user = request.user
            obj.author = user
        return super().save_model(request, obj, form, change)

class Block_Content_Admin(admin.ModelAdmin):
    list_display = ["blog", "block_type", "order"]
    list_editable = ["order"]

admin.site.register(Blog_Model, Blog_Admin)
admin.site.register(Block_Content_Model, Block_Content_Admin)