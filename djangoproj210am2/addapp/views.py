from django.shortcuts import render
from django.http import HttpResponse
def input(request):
    return render(request,'base.html')
def add(request):
    try:
        a=request.POST["t1"]
        x=int(a)
        b=request.POST["t2"]
        y=int(b)
        z=x+y
        return HttpResponse("<html><body bgcolor=green><h1>sum is= "+ str(z)+"</h1></body></html>")
    except(ValueError):
        return HttpResponse("invalidinput")

# Create your views here.
