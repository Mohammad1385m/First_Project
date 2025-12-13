from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import *

from Order_App.models import OrderModel
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
    user = request.user
    cart = OrderModel.objects.filter(user=user, is_paid=False).prefetch_related("orderdetails_set").first()
    total_payment = 0
    for order in cart.orderdetails_set.all():
        discount_value = order.final_price - (order.final_price * (order.off / 100))
        total_payment += int(round(discount_value, 0)) * order.count
    return render(request, "Header.html", {
        "categories_in_dropdown": categories_in_dropdown,
        "brands_in_dropdown": brands_in_dropdown,
        "site_settings": site_settings,
        "cart": cart,
        "total_payment": total_payment
    })


def footer_component(request):
    return render(request, "Footer.html", {
        "site_settings": site_settings
    })
