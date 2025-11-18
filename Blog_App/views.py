from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse
from django.views import *
from django.views.decorators.csrf import csrf_exempt

from .models import *
from .forms import *


# Create your views here.

class Blog_List_View(View):
    def get(self, request):
        blogs = Blog_Model.objects.filter(is_published=True).order_by("-create_at")
        return render(request, "blog.html", {
            "blogs": blogs,
        })


class Blog_Detail_View(View):
    def get(self, request, slug):
        a_single_blog = Blog_Model.objects.filter(slug=slug).first()
        a_s_b_contents = Block_Content_Model.objects.filter(blog=a_single_blog).order_by("order")
        a_s_b_comments = Blog_Comment.objects.filter(blog=a_single_blog, is_active=True).order_by("-create_at")
        comment_form = Comment_Form()
        return render(request, "blogSingle.html", {
            "a_s_b": a_single_blog,
            "contents": a_s_b_contents,
            "comments": a_s_b_comments,
            "comment_form": comment_form
        })

    def post(self, request, slug):
        comment_form = Comment_Form(request.POST)
        user = request.user
        a_single_blog = Blog_Model.objects.filter(slug=slug).first()
        text = request.POST["text"]
        new_comment = Blog_Comment(text=text, user=user, blog=a_single_blog)
        new_comment.save()
        return redirect("home")
            # messages.success(request, "Your comment has been added.")
            # return redirect(reverse("blog_detail", args=[a_single_blog.slug]))


@csrf_exempt
def send_comment(request):
    if request.method == "POST":
        try:
            blog_id = int(request.POST.get("blog_id"))
            text = request.POST.get("text")
            if blog_id and text:
                new_comment = Blog_Comment(user=request.user, text=text, blog_id=blog_id)
                new_comment.save()
                return JsonResponse({"status": "comment created"}, status=201)
            else:
                return JsonResponse({"status": "error"}, status=400)
        except Exception as e:
            return JsonResponse({"status": str(e)}, status=400)
