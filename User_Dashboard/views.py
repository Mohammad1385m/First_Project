from django.shortcuts import render, redirect
from django.views import View

from Order_App.models import *


# Create your views here.

class User_Dashboard(View):
    def get(self, request):
        if request.user.is_authenticated:
            pass
        else:
            return redirect("login-register")
        all_orders = OrderModel.objects.filter(user=request.user).order_by('-id')
        paid_orders = OrderModel.objects.filter(user=request.user, is_paid=True).order_by('-id')[:4]
        return render(request, "dashboard.html", {
            "all_orders": all_orders,
            "paid_orders": paid_orders
        })


class Orders_Dashboard(View):
    def get(self, request):
        if request.user.is_authenticated:
            pass
        else:
            return redirect("login-register")
        paid_orders = OrderModel.objects.filter(user=request.user, is_paid=True).order_by('-id')
        return render(request, "dashboardOrders.html", {
            "paid_orders": paid_orders
        })


class Order_Details_Dashboard(View):
    def get(self, request, id):
        if request.user.is_authenticated:
            pass
        else:
            return redirect("login-register")
        order = OrderModel.objects.filter(user=request.user, is_paid=True, id=id).first()
        return render(request, "dashboardOrdersDetails.html", {
            "order": order
        })
