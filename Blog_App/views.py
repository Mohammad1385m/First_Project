from django.shortcuts import render
from django.views import *
from .models import *


# Create your views here.

class Blog_List_View(View):
    def get(self, request):
        blogs = Blog_Model.objects.filter(is_published=True).order_by("-create_at")
        return render(request, "blog.html", {
            "blogs": blogs
        })

class Blog_Detail_View(View):
    def get(self, request, slug):
        a_single_blog = Blog_Model.objects.filter(slug=slug).first()
        return render(request, "blogSingle.html", {
            "a_s_l" : a_single_blog
        })