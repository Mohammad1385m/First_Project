from django.urls import path
from Blog_App.views import *

urlpatterns = [
    path("", Blog_List_View.as_view(), name="blog_list"),
    path("<PSlug:slug>/", Blog_Detail_View.as_view(), name="blog_detail"),
    path("send-comment/", send_comment, name="send_comment"),
]