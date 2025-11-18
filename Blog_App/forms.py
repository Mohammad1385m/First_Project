from django import forms
from .models import *


class Comment_Form(forms.ModelForm):
    class Meta:
        model = Blog_Comment
        fields = ["text"]
        widgets = {
            "text": forms.Textarea(attrs={
                "id": "textarea_comment", "class": "rounded-2xl rounded-tr-sm text-sm text-zinc-600 w-full bg-white border border-zinc-200 px-5 py-3.5 placeholder:text-zinc-400 placeholder:text-xs focus:outline-1 focus:outline-zinc-300",
                "placeholder":"متن دیدگاه"
            })
        }


# class Login_Form(forms.Form):
#     username = forms.CharField(widget=forms.TextInput(attrs={
#         "class": "rounded-2xl rounded-tr-sm text-sm text-zinc-600 w-full bg-[#f0f0f0] px-5 py-3.5 placeholder:text-zinc-400 placeholder:text-xs focus:outline-1 focus:outline-zinc-300",
#         "placeholder": "نام..."
#         }))
#     email = forms.EmailField(widget=forms.EmailInput(attrs={
#         "class": "rounded-2xl rounded-tr-sm text-sm text-zinc-600 w-full bg-[#f0f0f0] px-5 py-3.5 placeholder:text-zinc-400 placeholder:text-xs focus:outline-1 focus:outline-zinc-300",
#         "placeholder": "ایمیل..."
#         }))
#     password = forms.CharField(widget=forms.PasswordInput(attrs={
#         "class": "rounded-2xl rounded-tr-sm text-sm text-zinc-600 w-full bg-[#f0f0f0] px-5 py-3.5 placeholder:text-zinc-400 placeholder:text-xs focus:outline-1 focus:outline-zinc-300",
#         "placeholder": "رمز عبور..."
#         }))


# class Login_Form(forms.ModelForm):
#     class Meta:
#         model = User_Model
#         fields = ("username", "email", "password")
#         widgets = {
#             "username": forms.TextInput(attrs={
#                 "class": "rounded-2xl rounded-tr-sm text-sm text-zinc-600 w-full bg-[#f0f0f0] px-5 py-3.5 placeholder:text-zinc-400 placeholder:text-xs focus:outline-1 focus:outline-zinc-300",
#                 "placeholder": "نام..."
#             }),
#             "email": forms.EmailInput(attrs={
#                 "class": "rounded-2xl rounded-tr-sm text-sm text-zinc-600 w-full bg-[#f0f0f0] px-5 py-3.5 placeholder:text-zinc-400 placeholder:text-xs focus:outline-1 focus:outline-zinc-300",
#                 "placeholder": "ایمیل..."
#             }),
#             "password": forms.PasswordInput(attrs={
#                 "class": "rounded-2xl rounded-tr-sm text-sm text-zinc-600 w-full bg-[#f0f0f0] px-5 py-3.5 placeholder:text-zinc-400 placeholder:text-xs focus:outline-1 focus:outline-zinc-300",
#                 "placeholder": "رمز عبور..."
#             })
#         }
