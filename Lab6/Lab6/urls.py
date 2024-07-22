from django.contrib import admin
from django.urls import path
from core.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path("",ListV.as_view(),name="ListV"),
    path("detail/<int:pk>",DetailV.as_view(),name="detail")
]
