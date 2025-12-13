from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views import View

from Order_App.models import *


# Create your views here.

class CartView(View):
    def get(self, request):
        if request.user.is_authenticated:
            user = request.user
            cart = OrderModel.objects.filter(user=user, is_paid=False).prefetch_related("orderdetails_set").first()
            total_amount = 0
            for item in cart.orderdetails_set.all():
                total_amount += int(round((item.final_price * item.count) - ((item.final_price * item.off) / 100), 0))
            final_payable_price = total_amount

            if cart is not None:
                return render(request, "cart.html", {
                    "user": user,
                    "cart": cart,
                    "final_payable_price": final_payable_price
                })
            else:
                return render(request, "cart.html", {
                    "user": user,
                })
        else:
            pass


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
                new_order_details = OrderDetails(order=order, product=product, count=product_count, off=product.off,
                                                 final_price=product.price)
                new_order_details.save()

            return JsonResponse({
                "status": "success"
            })
        else:
            return JsonResponse({
                "status": "unauthorized"
            })
