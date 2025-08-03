from django import forms
from .models import Contact_Us_Model

class Contact_Us_Form(forms.ModelForm):
    class Meta:
        model = Contact_Us_Model
        fields = ["name", "phone", "email", "subject", "message"]
        widgets = {
            "name": forms.TextInput(
                attrs={
                    "class": "rounded-2xl rounded-tr-sm text-sm text-zinc-600 w-full bg-[#f0f0f0] px-5 py-3.5 placeholder:text-zinc-400 placeholder:text-xs focus:outline-1 focus:outline-zinc-300", "value": "moha", "placeholder": "نام..."
                }
            ),
            "phone": forms.TextInput(
                attrs={
                    "class": "rounded-2xl rounded-tr-sm text-sm text-zinc-600 w-full bg-[#f0f0f0] px-5 py-3.5 placeholder:text-zinc-400 placeholder:text-xs focus:outline-1 focus:outline-zinc-300", "value": "09962381904", "placeholder": "شماره تلفن...",
                    "pattern": "[0-9]+"
                }
            ),
            "email": forms.EmailInput(
                attrs={
                    "class": "rounded-2xl rounded-tr-sm text-sm text-zinc-600 w-full bg-[#f0f0f0] px-5 py-3.5 placeholder:text-zinc-400 placeholder:text-xs focus:outline-1 focus:outline-zinc-300", "value": "moha@gmail.com", "placeholder": "ایمیل..."
                }
            ),
            "subject": forms.TextInput(
                attrs={
                    "class": "rounded-2xl rounded-tr-sm text-sm text-zinc-600 w-full bg-[#f0f0f0] px-5 py-3.5 placeholder:text-zinc-400 placeholder:text-xs focus:outline-1 focus:outline-zinc-300", "value": "help me", "placeholder": "موضوع..."
                }
            ),
            "message": forms.Textarea(
                attrs={
                    "class": "rounded-2xl rounded-tr-sm text-sm text-zinc-600 w-full bg-[#f0f0f0] px-5 py-3.5 placeholder:text-zinc-400 placeholder:text-xs focus:outline-1 focus:outline-zinc-300 resize-none", "value": "i need your help", "placeholder": "متن پیام..."
                }
            )
        }