from django.http import HttpResponse
from django.shortcuts import render
from Products_App.models import *

# Create your views here.

def product_list_in_home(request):
    return render(request, "Home_Page_Template.html", {})

def header_component(request):
    categories_in_dropdown = Product_Category.objects.filter(is_active=True)
    return render(request, "Header.html", {
        "categories_in_dropdown": categories_in_dropdown
    })

def footer_component(request):
    return render(request, "Footer.html", {})
