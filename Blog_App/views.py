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
        a_s_b_contents = Block_Content_Model.objects.filter(blog=a_single_blog).order_by("order")
        a_s_b_comments = Blog_Comment.objects.filter(blog=a_single_blog, is_published=True, is_active=True).order_by("-create_at")
        return render(request, "blogSingle.html", {
            "a_s_b" : a_single_blog,
            "contents" : a_s_b_contents,
            "comments" : a_s_b_comments
        })