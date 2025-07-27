from django.urls import path
from Products_App import views

urlpatterns = [
    path('', views.products_list, name="products_list"),
    path('<slug>/', views.product_detail, name="product_details"),
    path('categories/<slug>', views.category_content, name="category_content"),
    path('categories/subcategories/<slug>', views.sub_category_content, name="sub_category_content")

]