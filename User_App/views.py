from django.contrib.auth import login, logout
from django.contrib.auth.hashers import make_password
from django.contrib.messages.context_processors import messages
from django.http import Http404
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils import timezone
from django.utils.crypto import get_random_string
from django.views import View
from django.core.cache import cache
from services.email_service.otp_email import send_otp
from .forms import *
from .models import *
from utils.utils import *
from django.contrib import messages

# Create your views here.

class Login_Register(View):
    def get(self, request):
        register_form = Register_Form()
        login_form = Login_Form()
        return render(request, "login-register.html", {
            "register_form": register_form,
            "login_form": login_form
        })

    def post(self, request):
        if "register" in request.POST:
            register_form = Register_Form(request.POST)
            login_form = Login_Form()
            if register_form.is_valid():
                username = register_form.cleaned_data.get("username")
                phone = register_form.cleaned_data.get("phone")
                email = register_form.cleaned_data.get("email")
                password = register_form.cleaned_data.get("password")
                otp = otp_generator(6)
                token = get_random_string(50)
                cached_data = {
                    "username": username,
                    "phone": phone,
                    "email": email,
                    "password": make_password(password),
                    "token": token,
                    "otp": otp,
                    "timestamp": timezone.now().timestamp()
                }
                cache_key = f"otp-{token}"
                send_otp(subject="Account Activation", to=email, context={"username": username, "otp": otp}, template_name="send_otp.html")
                cache.set(cache_key, cached_data, timeout=180)
                return redirect(reverse("otp", args=[token]))

        elif "login" in request.POST:
            print("runs login form")
            register_form = Register_Form()
            login_form = Login_Form(request.POST)

            if login_form.is_valid():
                print("form is valid")
                username = login_form.cleaned_data.get("username")
                email = login_form.cleaned_data.get("email")
                password = login_form.cleaned_data.get("password")
                user = User_Model.objects.filter(username=username, email=email).first()
                print(user)
                if user is not None:
                    print("user is not none")
                    if user.check_password(password):
                        print("user password is correct")
                        login(request, user)
                        return redirect("home")
            else:
                print("is not valid")

        return render(request, "login-register.html", {
            "register_form": register_form,
            "login_form": login_form
        })


class User_Dashboard(View):
    def get(self, request):
        return render(request, "dashboard.html", {})


class Otp_View(View):
    def get(self, request, token):
        cache_key = f"otp-{token}"
        cache_data = cache.get(cache_key)
        print(cache_data.get("otp"))
        if cache_data is not None:
            return render(request, "otp-page.html", {})
        else:
            return Http404

    def post(self, request, token):
        cache_key = f"otp-{token}"
        cache_data = cache.get(cache_key)
        if cache_data is not None:
            if timezone.now().timestamp() - cache_data.get("timestamp") < 180:
                otp1 = request.POST.get("otp1")
                otp2 = request.POST.get("otp2")
                otp3 = request.POST.get("otp3")
                otp4 = request.POST.get("otp4")
                otp5 = request.POST.get("otp5")
                otp6 = request.POST.get("otp6")
                user_otp = f"{otp1}{otp2}{otp3}{otp4}{otp5}{otp6}"
                if cache_data.get("otp") == user_otp:
                    user = User_Model(username=cache_data.get("username"), phone=cache_data.get("phone"), email=cache_data.get("email"), password=cache_data.get("password"))
                    user.token = get_random_string(50)
                    user.save()
                    login(request, user)
                    cache.delete(cache_key)
                    return redirect("home")
                else:
                    return render(request, "otp-page.html", {
                        "otp_matched": False
                    })
            else:
                return render(request, "otp-page.html", {
                    "expire": True
                })
        else:
            return render(request, "otp-page.html", {
                "error": True
            })

def user_logout(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect("home")