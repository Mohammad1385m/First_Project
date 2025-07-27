from django.shortcuts import render
from django.views import View

# Create your views here.

class Login_Register(View):
    def get(self, request):
        return render(request, "login-register.html", {

        })
    def post(self, request):
        pass
