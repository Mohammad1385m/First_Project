from django.urls import path
from User_Dashboard.views import *

urlpatterns = [
    path("", User_Dashboard.as_view(), name="dashboard"),
    path("orders/", Orders_Dashboard.as_view(), name="dashboard_orders"),
    path("orders/<id>/", Order_Details_Dashboard.as_view(), name="dashboard_order_details"),

]