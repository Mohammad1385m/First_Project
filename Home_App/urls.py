from django.urls import path
from Home_App.views import *

urlpatterns = [
    path('', Home_View.as_view(), name='home'),
    path('message', show_message, name='message'),
]