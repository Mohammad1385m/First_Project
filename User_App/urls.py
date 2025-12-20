from django.urls import path
from User_App.views import *

urlpatterns = [
    path("login-register/", Login_Register.as_view(), name="login_register"),
    path("logout/", user_logout, name="logout"),
    path("otp/<token>/", Otp_View.as_view(), name="otp"),
]