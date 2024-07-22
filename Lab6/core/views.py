from django.shortcuts import render
from django.views.generic import ListView,DetailView
from core.models import *

class ListV(ListView):
    model=Student
    template_name="index.html"

class DetailV(DetailView):
    model=Student
    template_name="student.html"
    