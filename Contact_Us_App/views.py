from django.shortcuts import render, redirect
from django.urls import reverse
from .models import *
from .forms import *


# Create your views here.

def contact_us_view(request):
    if request.method == "GET":
        form = Contact_Us_Form()
        return render(request, "contactUs.html",{
            "form": form
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