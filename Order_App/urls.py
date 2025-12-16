from django.urls import path
from .views import *

urlpatterns = [
    path("cart/", CartView.as_view(), name="cart"),
    path("add_to_basket/", add_to_basket, name="add_to_basket"),
    path("increase-quantity/", increase_quantity, name="increase_quantity"),
    path("decrease-quantity/", decrease_quantity, name="decrease_quantity"),
    path("delete-item/", delete_item, name="delete_item"),
]