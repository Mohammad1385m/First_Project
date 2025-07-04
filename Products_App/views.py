from django.http import HttpResponse
from django.shortcuts import render
from Products_App.models import *


# Create your views here.

def index(request):
    return "hi"
def products_list(request):
    pros = Product_Model.objects.all().order_by("-id")
    new_pros = pros[:3]
    return render(request, "Products_Page_Template.html", {
        "pros": pros,
        "new_pros": new_pros
    })


def product_detail(request, slug):
    a_single_product = Product_Model.objects.filter(slug=slug).first()
    return render(request, "Product_Detail_Page_Template.html", {"a_s_l": a_single_product})


def category_content(request, slug):
    a_single_category = Product_Category.objects.filter(slug=slug).first()
    products_in_category = Product_Model.objects.filter(category = a_single_category)
    return render(request, "Category_Content_Page_Template.html", {
        "a_s_c": a_single_category,
        "p_i_c": products_in_category
    })
