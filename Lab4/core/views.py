from django.shortcuts import render
from core.models import Student,Course
from django.http import HttpResponse

def home(request):
    if request.method == "POST":
        cid=request.POST.get("cid")
        sid=request.POST.get("sid")
        s_student=Student.objects.get(id=sid)
        c_course=Course.objects.get(id=cid)
        if s_student.enrollment.filter(id=cid).exists():
            return HttpResponse("<h1>Already Enrolled </h1> ")
        s_student.enrollment.add(c_course)
        return HttpResponse("<h1> Student enroll </h1> ")
    else:
        s_student=Student.objects.all()
        c_course=Course.objects.all()
        context={"students":s_student,"courses":c_course}
        return render(request,"home.html",context)
    



