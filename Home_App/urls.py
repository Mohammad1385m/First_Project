from django.urls import path
from Home_App import views

urlpatterns = [
    path('', views.product_list_in_home, name='home'),
]