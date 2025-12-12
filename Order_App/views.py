from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views import View

from Order_App.models import *


# Create your views here.

class CartView(View):
    def get(self, request):
        context = {}
        return render(request, "cart.html", context)


def add_to_basket(request):
    if request.method == "GET":
        print()
        if request.user.is_authenticated:
            product_id = request.GET.get("product_id")
            product_count = request.GET.get("product_count")
            try:
                product_id = int(product_id)
                product = Product_Model.objects.filter(id=product_id).first()
                product_count = int(product_count)
            except:
                JsonResponse({
                    "status": "not_valid"
                })

            order, _ = OrderModel.objects.get_or_create(user=request.user, is_paid=False)
            order_details = OrderDetails.objects.filter(order=order, product=product).first()
            if order_details:
                order_details.count += product_count
                order_details.save()
            else:
                new_order_details = OrderDetails(order=order, product=product, count=product_count, off=product.off)
                new_order_details.save()

            return JsonResponse({
                "status": "success"
            })
        else:
            return JsonResponse({
                "status": "unauthorized"
            })
