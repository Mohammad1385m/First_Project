from django.urls import path
from .views import *

urlpatterns = [
    path("cart/", CartView.as_view(), name="cart"),
    path("add_to_basket/", add_to_basket, name="add_to_basket"),
]