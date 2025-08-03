from django import forms
from .models import *


class Register_Form(forms.ModelForm):
    class Meta:
        model = User_Model
        fields = ("username", "phone", "email", "password")
        widgets = {
            "username": forms.TextInput(attrs={
                "class": "rounded-2xl rounded-tr-sm text-sm text-zinc-600 w-full bg-[#f0f0f0] px-5 py-3.5 placeholder:text-zinc-400 placeholder:text-xs focus:outline-1 focus:outline-zinc-300",
                "placeholder": "نام..."
            }),
            "phone": forms.TextInput(attrs={
                "class": "rounded-2xl rounded-tr-sm text-sm text-zinc-600 w-full bg-[#f0f0f0] px-5 py-3.5 placeholder:text-zinc-400 placeholder:text-xs focus:outline-1 focus:outline-zinc-300",
                "placeholder": "شماره تلفن...", "pattern": "[0-9]+"
            }),
            "email": forms.EmailInput(attrs={
                "class": "rounded-2xl rounded-tr-sm text-sm text-zinc-600 w-full bg-[#f0f0f0] px-5 py-3.5 placeholder:text-zinc-400 placeholder:text-xs focus:outline-1 focus:outline-zinc-300",
                "placeholder": "ایمیل..."
            }),
            "password": forms.PasswordInput(attrs={
                "class": "rounded-2xl rounded-tr-sm text-sm text-zinc-600 w-full bg-[#f0f0f0] px-5 py-3.5 placeholder:text-zinc-400 placeholder:text-xs focus:outline-1 focus:outline-zinc-300",
                "placeholder": "رمز عبور..."
            })
        }


class Login_Form(forms.ModelForm):
    class Meta:
        model = User_Model
        fields = ("username", "email", "password")
        widgets = {
            "username": forms.TextInput(attrs={
                "class": "rounded-2xl rounded-tr-sm text-sm text-zinc-600 w-full bg-[#f0f0f0] px-5 py-3.5 placeholder:text-zinc-400 placeholder:text-xs focus:outline-1 focus:outline-zinc-300",
                "placeholder": "نام..."
            }),
            "email": forms.EmailInput(attrs={
                "class": "rounded-2xl rounded-tr-sm text-sm text-zinc-600 w-full bg-[#f0f0f0] px-5 py-3.5 placeholder:text-zinc-400 placeholder:text-xs focus:outline-1 focus:outline-zinc-300",
                "placeholder": "ایمیل..."
            }),
            "password": forms.PasswordInput(attrs={
                "class": "rounded-2xl rounded-tr-sm text-sm text-zinc-600 w-full bg-[#f0f0f0] px-5 py-3.5 placeholder:text-zinc-400 placeholder:text-xs focus:outline-1 focus:outline-zinc-300",
                "placeholder": "رمز عبور..."
            })
        }
