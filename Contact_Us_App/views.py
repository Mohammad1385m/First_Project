from django.shortcuts import render, redirect


# Create your views here.

def contact_us_view(request):
    if request.method == "GET":
        return render(request, "contactUs.html",{})
    elif request.method == "POST":
        name = request.POST.get("full_name")
        return redirect("home")