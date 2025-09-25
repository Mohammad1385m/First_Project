from django.http import HttpResponse
from django.shortcuts import render
from Products_App.models import *


# Create your views here.

def products_list(request):
    pros = Product_Model.objects.filter(is_active=True).order_by("-id")
    new_pros = pros[:3]
    return render(request, "shop.html", {
        "pros": pros,
        "new_pros": new_pros
    })


def product_detail(request, slug):
    a_single_product = Product_Model.objects.filter(slug=slug).first()
    pro_color = Product_Color.objects.filter(product_model=a_single_product)
    pro_extra_images = Product_Extra_Images.objects.filter(product=a_single_product)
    return render(request, "singleProduct.html", {
        "a_s_p": a_single_product,
        "pro_color": pro_color,
        "pro_extra_images": pro_extra_images,
    })


def category_content(request, slug):
    a_single_category = Product_Category.objects.filter(slug=slug).first()
    products_in_category = Product_Model.objects.filter(subcategory__category=a_single_category)
    return render(request, "categoryContent.html", {
        "a_s_c": a_single_category,
        "p_i_c": products_in_category
    })


def sub_category_content(request, slug):
    a_single_subcategory = Product_SubCategory.objects.filter(slug=slug).first()
    products_in_subcategory = Product_Model.objects.filter(subcategory=a_single_subcategory)
    return render(request, "categoryContent.html", {
        "a_s_s": a_single_subcategory,
        "p_i_c": products_in_subcategory
    })
