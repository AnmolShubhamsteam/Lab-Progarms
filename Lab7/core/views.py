from django.shortcuts import render
from django.http import HttpResponse
from core.models import Student
import csv
from reportlab.pdfgen.canvas import Canvas

def home(request):
    return render(request,"index.html")

def dcsv(request):
    response=HttpResponse(content_type="text/csv")
    response["Content-Disposition"]='attachment; filename="student.csv"'
    writer=csv.writer(response)
    writer.writerow(["Name","USN"])
    Students=Student.objects.all().values_list("name","usn")
    for s in Students:
        writer.writerow(s)
    return response

def dpdf(request):
    response=HttpResponse(content_type="application/pdf")
    studnets=Student.objects.all()
    response["Content-Disposition"]='attachment; filename="student.pdf"'
    c=Canvas(response)
    c.drawString(70,720,"name")
    c.drawString(170,720,"usn")
    y=660
    for s in studnets:
        c.drawString(70,y,s.name)
        c.drawString(170,y,s.usn)
        y=y-60
    c.showPage()
    c.save()
    return response