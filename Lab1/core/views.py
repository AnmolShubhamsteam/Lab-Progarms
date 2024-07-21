from django.shortcuts import render
from django.http import HttpResponse as HR
from datetime import datetime,timedelta

def index(request):
    t = datetime.now()
    t1 = t + timedelta(hours=4)
    t2 = t - timedelta(hours=4)
    response = f"""
    <h1>NOW = {t}</h1>
    <h1>NOW + 4 HOURS = {t1}</h1>
    <h1>NOW - 4 HOURS = {t2}</h1>
    """
    return HR(response)