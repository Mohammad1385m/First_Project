from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import *
from Products_App.models import *
from django.contrib import messages

# Create your views here.

class Home_View(View):
    def get(self, request):
        context = {
            "products": self.product_list_in_slider1()
        }
        return render(request, "index.html", context)

    def product_list_in_slider1(self):
        products_in_slider_1 = Product_Model.objects.filter(is_active=True).order_by("-id")[:5]
        return products_in_slider_1

def show_message(request):
    messages.success(request, "Home View Page")
    return redirect("home")

def header_component(request):
    categories_in_dropdown = Product_Category.objects.filter(is_active=True)
    sub_categories_in_dropdown = Product_SubCategory.objects.filter(is_active=True)
    return render(request, "Header.html", {
        "categories_in_dropdown": categories_in_dropdown,
        "sub_categories_in_dropdown": sub_categories_in_dropdown
    })

def footer_component(request):
    return render(request, "Footer.html", {})
