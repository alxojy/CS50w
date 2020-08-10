from django.http import HttpResponse
from django.shortcuts import render

def index0(request):
    return HttpResponse("Hello, world!")

def index1(request):
    return render(request, "hello/index.html")

def brian(request):
    return HttpResponse("Hello, Brian!")

def david(request):
    return HttpResponse("Hello, David!")

def greet0(request, name):
    return HttpResponse(f"Hello, {name.capitalize()}!")

def greet1(request, name):
    return render(request, "hello/greet.html", {
        "name": name.capitalize()
    })