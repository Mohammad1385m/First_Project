from django.http import HttpResponse
from django.shortcuts import render
from unicodedata import category

from Products_App.models import *


# Create your views here.

def products_list(request):
    pros = Product_Model.objects.filter(is_active=True).order_by("-id")
    brands = BrandModel.objects.filter(is_active=True).order_by("-id")
    categories = Product_Category.objects.filter(is_active=True).order_by("-id")
    new_pros = pros[:3]
    return render(request, "shop.html", {
        "pros": pros,
        "brands": brands,
        "categories": categories,
        "new_pros": new_pros
    })


def product_detail(request, slug):
    a_single_product = Product_Model.objects.filter(slug=slug).first()
    similar_products = Product_Model.objects.filter(is_active=True, brand=a_single_product.brand).exclude(id=a_single_product.id)
    pro_color = Product_Color.objects.filter(product_model=a_single_product)
    pro_extra_images = Product_Extra_Images.objects.filter(product=a_single_product)
    return render(request, "singleProduct.html", {
        "a_s_p": a_single_product,
        "pro_color": pro_color,
        "pro_extra_images": pro_extra_images,
        "similar_products": similar_products
    })


def category_content(request, slug):
    a_single_category = Product_Category.objects.filter(slug=slug).first()
    products_in_category = Product_Model.objects.filter(category=a_single_category)
    return render(request, "categoryContent.html", {
        "a_s_c": a_single_category,
        "p_i_c": products_in_category
    })


def brand_content(request, slug):
    a_single_brand = BrandModel.objects.filter(slug=slug).first()
    products_in_brand = Product_Model.objects.filter(brand=a_single_brand)
    return render(request, "categoryContent.html", {
        "a_s_b": a_single_brand,
        "p_i_b": products_in_brand
    })
