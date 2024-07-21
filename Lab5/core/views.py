from django.shortcuts import render,redirect
from core.forms import ProjectForm


def index(request):
    return render(request,"index.html")

def home(request):
    Form=ProjectForm()
    if request.method == "POST":
        Form=ProjectForm(request.POST)
        if Form.is_valid():
            Form.save()
        return redirect("index")
    return render(request,"form.html",{"form":Form})
