from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import *
from Products_App.models import *
from Site_Settings_App.models import *
from django.contrib import messages

# Create your views here.

site_settings = SiteSettingsModel.objects.filter(is_active=True).first()
class Home_View(View):
    def get(self, request):
        main_slider_content = Sliders.objects.filter(slider_type="main_slider")
        context = {
            "products": self.product_list_in_slider1(),
            "main_slider_content": main_slider_content
        }
        return render(request, "index.html", context)

    def product_list_in_slider1(self):
        products_in_slider_1 = Product_Model.objects.filter(is_active=True).order_by("-id")[:5]
        return products_in_slider_1

def show_message(request):
    messages.success(request, "به صفحه اصلی منتقل شدید")
    return redirect("home")

def header_component(request):
    categories_in_dropdown = Product_Category.objects.filter(is_active=True)
    brands_in_dropdown = BrandModel.objects.filter(is_active=True)
    return render(request, "Header.html", {
        "categories_in_dropdown": categories_in_dropdown,
        "brands_in_dropdown": brands_in_dropdown,
        "site_settings": site_settings
    })

def footer_component(request):
    return render(request, "Footer.html", {
        "site_settings": site_settings
    })
