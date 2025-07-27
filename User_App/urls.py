from django.urls import path
from User_App import views
from User_App.views import Login_Register

urlpatterns = [
    path("login-register", Login_Register.as_view(), name="login_register"),
]