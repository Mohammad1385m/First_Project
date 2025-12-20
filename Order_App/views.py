from django.contrib.admin import action
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.views import View
from Order_App.models import *


# Create your views here.

class CartView(View):
    def get(self, request):
        if request.user.is_authenticated:
            try:
                user = request.user
                cart = OrderModel.objects.filter(user=user, is_paid=False).prefetch_related("orderdetails_set").first()
                total_amount = 0

                if cart is not None:
                    for item in cart.orderdetails_set.all():
                        total_amount += (item.final_price - ((item.final_price / 100) * item.off)) * item.count

                    final_payable_price = int(round(total_amount, 0))
                    return render(request, "cart.html", {
                        "user": user,
                        "cart": cart,
                        "final_payable_price": final_payable_price
                    })
                else:
                    return render(request, "cart.html", {
                        "user": user,
                    })
            except:
                return redirect("home")
        else:
            pass


def add_to_basket(request):
    if request.method == "GET":
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
            final_price = product.price - ((product.price * product.off) / 100)

            if order_details:
                order_details.count += product_count
                order_details.save()
            else:
                new_order_details = OrderDetails(order=order, product=product, count=product_count, off=product.off,
                                                 final_price=final_price)
                new_order_details.save()

            return JsonResponse({
                "status": "success"
            })
        else:
            return JsonResponse({
                "status": "unauthorized"
            })


def increase_quantity(request):
    if request.method == "GET":
        product_id = request.GET.get("product_id")
        try:
            product_id = int(product_id)
            product = Product_Model.objects.filter(id=product_id).first()
        except:
            return JsonResponse({
                "status": "not_valid"
            })
        order = OrderModel.objects.filter(user=request.user, is_paid=False).first()
        order_details = OrderDetails.objects.filter(order=order, product=product).first()
        order_details.count += 1
        order_details.save()

        user = request.user
        cart = OrderModel.objects.filter(user=user, is_paid=False).prefetch_related("orderdetails_set").first()
        total_amount = 0
        for item in cart.orderdetails_set.all():
            total_amount += (item.final_price - ((item.final_price / 100) * item.off)) * item.count

        final_payable_price = int(round(total_amount, 0))

        context = {
            "user": user,
            "cart": cart,
            "final_payable_price": final_payable_price
        }
        content = render_to_string("cartOrderDetails.html", context)
        return JsonResponse({
            "status": "increase",
            "content": content
        })


def decrease_quantity(request):
    if request.method == "GET":
        product_id = request.GET.get("product_id")

        try:
            product_id = int(product_id)
            product = Product_Model.objects.filter(id=product_id).first()
        except:
            return JsonResponse({
                "status": "not_valid"
            })
        order = OrderModel.objects.filter(user=request.user, is_paid=False).first()
        order_details = OrderDetails.objects.filter(order=order, product=product).first()

        if order_details.count > 1:
            order_details.count -= 1
            order_details.save()
            action = "decrease"
        elif order_details.count <= 1:
            action = "remove"
        user = request.user
        cart = OrderModel.objects.filter(user=user, is_paid=False).prefetch_related("orderdetails_set").first()
        total_amount = 0
        for item in cart.orderdetails_set.all():
            total_amount += (item.final_price - ((item.final_price / 100) * item.off)) * item.count

        final_payable_price = int(round(total_amount, 0))

        context = {
            "user": user,
            "cart": cart,
            "final_payable_price": final_payable_price,
        }
        content = render_to_string("cartOrderDetails.html", context)

        return JsonResponse({
            "status": action,
            "content": content
        })


def delete_item(request):
    if request.method == "GET":
        product_id = request.GET.get("product_id")

        try:
            product_id = int(product_id)
            product = Product_Model.objects.filter(id=product_id).first()
        except:
            return JsonResponse({
                "status": "not_valid"
            })
        order = OrderModel.objects.filter(user=request.user, is_paid=False).first()
        order_details = OrderDetails.objects.filter(order=order, product=product).first()
        order_details.delete()

        user = request.user
        cart = OrderModel.objects.filter(user=user, is_paid=False).prefetch_related("orderdetails_set").first()
        total_amount = 0
        for item in cart.orderdetails_set.all():
            total_amount += (item.final_price - ((item.final_price / 100) * item.off)) * item.count

        final_payable_price = int(round(total_amount, 0))

        context = {
            "user": user,
            "cart": cart,
            "final_payable_price": final_payable_price,
        }
        content = render_to_string("cartOrderDetails.html", context)

        return JsonResponse({
            "content": content
        })
