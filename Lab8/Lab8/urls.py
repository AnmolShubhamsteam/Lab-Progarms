from django.contrib import admin
from django.urls import path
from core.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",user_login,name="login"),
    path("index/",index,name="index"),
]
