from django.shortcuts import render, redirect
from django.urls import reverse
from .models import *
from Site_Settings_App.models import *
from .forms import *


# Create your views here.

def contact_us_view(request):
    if request.method == "GET":
        form = Contact_Us_Form()
        site_settings = SiteSettingsModel.objects.filter(is_active=True).first()
        return render(request, "contactUs.html",{
            "form": form,
            "site_settings": site_settings
        })
    elif request.method == "POST":
        form = Contact_Us_Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
        else:
            return render(request, "contactUs.html", {
                "form": form,
            })