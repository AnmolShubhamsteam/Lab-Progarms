from django.shortcuts import render

def index(request):
    li=['a','b','c','d']
    li2=['x','y','z','w']
    context={"li":li,"li2":li2}
    return render(request,"index.html",context)
